#!/usr/bin/env python3
"""
HiggsField Creative Ads — batch runner
Usage: python3 gen_run.py <plan.json>

plan.json format:
{
  "model": "gpt_image_2",
  "max_concurrent": 6,
  "resolution": "2k",
  "log": "./gen.log",
  "items": [
    {
      "id": "s01-hook-a",
      "aspect": "3:4",
      "prompt": "...",
      "outdir": "./singles"
    }
  ]
}

Models: gpt_image_2 (7 credits, best text rendering), nano_banana_2 (2 credits, supports 4:5)
Note: GPT Image 2 does NOT support 4:5 — use 3:4 for feed portrait.
"""
import json, sys, subprocess, time, re, os, urllib.request

plan = json.load(open(sys.argv[1]))
MODEL = plan.get("model", "gpt_image_2")
MAXC = plan.get("max_concurrent", 6)
RES = plan.get("resolution", "2k")
items = plan["items"]
LOG = plan.get("log", "./gen.log")


def log(m):
    line = f"{time.strftime('%H:%M:%S')} {m}"
    print(line, flush=True)
    open(LOG, "a").write(line + "\n")


def run(args, t=180):
    try:
        return subprocess.run(args, capture_output=True, text=True, timeout=t)
    except Exception as e:
        class R:
            stdout = ""
            stderr = str(e)
        return R()


log(f"=== START model={MODEL} items={len(items)} max_concurrent={MAXC} res={RES} ===")

# Skip already-done items
todo = []
for it in items:
    out = os.path.join(it["outdir"], f"{it['id']}.png")
    if os.path.exists(out) and os.path.getsize(out) > 50_000:
        log(f"{it['id']} already done, skip")
    else:
        os.makedirs(it["outdir"], exist_ok=True)
        todo.append(it)

log(f"{len(todo)} items to generate")


def create_job(it):
    args = [
        "higgsfield", "generate", "create", MODEL,
        "--prompt", " ".join(it["prompt"].split()),
        "--aspect_ratio", it.get("aspect", "3:4"),
        "--resolution", RES,
    ]
    if it.get("image"):
        # Note: with gpt_image_2, --image suppresses text rendering — use prompt-only
        args += ["--image", it["image"]]
    if MODEL in ("gpt_image_2", "imagegen_2_0"):
        args += ["--quality", "high"]
    args += ["--json"]

    r = run(args, 150)
    txt = (r.stdout or "") + (r.stderr or "")

    if "concurrent_jobs_limit" in txt:
        return None, "limit"
    # Both gpt_image_2 {"id":"uuid"} and nano_banana_2 ["uuid"] — parse with generic UUID regex
    m = re.search(r"([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})", txt)
    return (m.group(1) if m else None), (txt[:200] if not m else "")


def job_state(jid):
    r = run(["higgsfield", "generate", "get", jid, "--json"], 60)
    txt = r.stdout or ""
    st = re.search(r'"status"\s*:\s*"(\w+)"', txt)
    url = re.findall(r"https://\S+?\.(?:png|jpg|jpeg|webp)", txt)
    return (st.group(1) if st else "?"), (url[-1] if url else "")


def download(it, url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    data = urllib.request.urlopen(req, timeout=90).read()
    path = os.path.join(it["outdir"], f"{it['id']}.png")
    open(path, "wb").write(data)
    return len(data)


inflight = {}
queue = list(todo)
ok = 0
deadline = time.time() + 3600  # 1h max

while (queue or inflight) and time.time() < deadline:
    # Fill slots up to max_concurrent
    while queue and len(inflight) < MAXC:
        it = queue[0]
        jid, err = create_job(it)
        if jid:
            inflight[jid] = it
            queue.pop(0)
            log(f"{it['id']} → job {jid[:8]} ({len(inflight)} in flight)")
        elif err == "limit":
            log(f"concurrent limit hit, waiting (in flight={len(inflight)})")
            break
        else:
            log(f"{it['id']} create failed: {err}")
            queue.pop(0)
        time.sleep(2)

    time.sleep(15)

    for jid, it in list(inflight.items()):
        st, url = job_state(jid)
        if st == "completed" and url:
            try:
                sz = download(it, url)
                log(f"{it['id']} OK ({sz:,} bytes)")
                ok += 1
            except Exception as e:
                log(f"{it['id']} download failed: {e}")
            del inflight[jid]
        elif st in ("failed", "error", "canceled"):
            log(f"{it['id']} job {st}")
            del inflight[jid]

if queue or inflight:
    remaining = [i["id"] for i in queue] + [it["id"] for it in inflight.values()]
    log(f"WARNING — not completed: {remaining}")

log(f"=== END ok={ok}/{len(todo)} ===")
print(f"Done: {ok}/{len(todo)}")

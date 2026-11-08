#!/usr/bin/env python3

import argparse
import datetime as dt
import json
import sys

import requests

import config

URL = f"http://{config.HOST}:{config.PORT}"
APPEALS_PER_TRIAL = 5
TEXT = (
    "I wrote this paragraph to test the appeal path. It has enough words and "
    "sentences for both signals to read it properly. The label it gets does not "
    "matter here, only what happens after the appeal is sent."
)


def one_appeal(trial, i):
    creator = f"eval_appeal_t{trial}_{i}"
    sub = requests.post(f"{URL}/submit", json={"text": TEXT, "creator_id": creator},
                        timeout=90)
    if sub.status_code != 200:
        return {"passed": False, "step": "submit", "status": sub.status_code,
                "body": sub.text[:300]}
    content_id = sub.json()["content_id"]

    app = requests.post(f"{URL}/appeal", json={
        "content_id": content_id,
        "reasoning": f"Eval trial {trial}, appeal {i}: I wrote this myself.",
    }, timeout=30)
    try:
        app_body = app.json()
    except ValueError:
        app_body = {"not_json": app.text[:300]}

    entries = requests.get(f"{URL}/log", timeout=30).json()["entries"]
    appeal_entries = [e for e in entries
                      if e.get("content_id") == content_id and e.get("event") == "appeal"]

    passed = (app.status_code == 200
              and app_body.get("status") == "under_review"
              and len(appeal_entries) == 1)
    return {
        "passed": passed,
        "content_id": content_id,
        "appeal_status_code": app.status_code,
        "appeal_response": app_body,
        "appeal_entries_in_log": len(appeal_entries),
        "log_entry": appeal_entries[0] if appeal_entries else None,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--label", default="")
    args = parser.parse_args()

    try:
        requests.get(f"{URL}/health", timeout=5)
    except Exception:  # noqa: BLE001
        sys.exit(f"Nothing answering at {URL}. Start it:  python app.py")

    trials = []
    for trial in range(1, args.trials + 1):
        results = [one_appeal(trial, i) for i in range(1, APPEALS_PER_TRIAL + 1)]
        passed = sum(r["passed"] for r in results)
        print(f"trial {trial}: {passed}/{APPEALS_PER_TRIAL} passed")
        trials.append(results)

    config.RESULTS_DIR.mkdir(exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    label = f"_{args.label}" if args.label else ""
    path = config.RESULTS_DIR / f"appeals_{stamp}{label}.md"

    lines = [f"# Criterion 4: appeals{f' — {args.label}' if args.label else ''}", "",
             "- Produced by: `run_appeals.py::main`",
             "- Service: `app.py::submit`, `app.py::appeal`, `app.py::get_log`", ""]
    for n, results in enumerate(trials, 1):
        passed = sum(r["passed"] for r in results)
        lines += [f"## Trial {n}: {passed}/{APPEALS_PER_TRIAL}", "", "```json",
                  json.dumps(results, indent=2), "```", ""]
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nWrote {path.relative_to(config.ROOT)}")


if __name__ == "__main__":
    main()
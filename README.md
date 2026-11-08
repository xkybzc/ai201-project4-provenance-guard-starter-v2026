# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->
A writer's text arrives at submit with a creator_id. The route first checks it: missing, empty, or over 2000 characters gets a 400 and nothing is logged. Valid text goes through two signals: detector.model_signal (a local GPT-2 model measuring how predictable the words are) and stylometry.style_signal (sentence-length spread, word variety, and punctuation density).
scoring.combine_signals blends them into one score, 80% model and 20% style, and scoring.score_to_label turns that score into one of three plain-English labels using the thresholds in config.py (0.35 and 0.65). The decision, with both signal scores, is appended to logs/audit.jsonl and returned to the writer with a content_id. If they think it's wrong, appeal with that id records their reasoning and moves the item to under_review next to the original decision.


---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:**How predictable the text is to a language model. GPT-2
reads the text, and the signal reports how little each next word surprised it,
scaled from 0 to 1. Low surprise gives a high score.

**Why that might differ between human and AI writing:**AI text is made by
picking likely next words, so another language model finds it easy to predict.
People choose odd words, break patterns, mention things the model has never
seen, and write about their own lives.

**What it can't see:**It can't see who wrote the text, only how expected the
words are. AI text that a person has roughed up with edits, odd
phrasing or typos scores lower, even though a machine wrote almost all of it.

### Signal two — the style signal

**What it measures:**The shape of the text, not its content. It measures how
much sentence length varies, the ratio of unique words to total words, and how
dense the punctuation is, and it combines them into one score from 0 to 1.

**Why that might differ between human and AI writing:**AI text tends toward
even sentence lengths, steady vocabulary and regular punctuation. People mix
short and long sentences, repeat themselves or reach for rare words, and use
punctuation unevenly.

**What it can't see:**It never reads what the words mean. It only counts them.
Adding typos raises the unique-word ratio and makes AI text look more human.
Splitting a few long sentences changes the spread without changing any content.
It also wrongly flags people who happen to write evenly, and on short texts the
counts are too noisy to mean much.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:**I take a weighted average of the two scores, 80% model signal and 20% style
signal. The model signal leads because it was the only signal that clearly
separated my test pieces, and the style signal can't read the text, so cheap
changes like typos can move it.

**The numbers:**- Weights: model 0.8, style 0.2

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**My clearly AI test piece scored 0.8649 on the model signal and 0.3286 on the
style signal, a gap of 0.54. The rule gives it 0.758: the style signal pulls
the model's score down by about 0.11 but doesn't override it.



---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.35 | We think this was written by a person. No action is needed. |
| unsure | 0.35 – 0.65 | We couldn't tell whether this was written by a person or with an AI tool. Nothing happens to your piece because of this. If you'd like, you can tell us about how you wrote it. |
| high-confidence AI | 0.65 – 1.00 | We think this was probably written with an AI tool. If you wrote it yourself, you can appeal and a person will review it. |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->
I wrote “we couldn’t tell” instead of “this may be AI” because the uncertainty belongs to my system, not the writer, and most people who land in this range probably wrote their own work. I said plainly that nothing happens to the piece, because an unsure label with no stated consequence feels like a warning. Finally I offered a way to tell us how they wrote it, so the label ends with something they can do rather than something done to them.



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->
```bash
$ curl.exe -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @valid.json
```

```json
{
  "confidence": 0.1727,
  "content_id": "fd5cd03b3f74",
  "creator_id": "khoi",
  "guess": "unsure",
  "label": "not built yet",
  "model_score": 0.1727,
  "style_score": null
}
```

**An appeal**

```bash
$ curl.exe -X POST http://127.0.0.1:5000/appeal -H "Content-Type: application/json" -d @appeal.json
```

```json
{
  "content_id": "6f274b1c4d99",
  "message": "Thanks \u2014 your appeal has been recorded and a person will review it.",
  "recorded_at": "2026-11-02T00:51:46+00:00",
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": null,
      "content_id": "c3c975928dc1",
      "creator_id": "khoi",
      "guess": null,
      "label": null,
      "model_score": 0.1727,
      "status": "decided",
      "style_score": null,
      "timestamp": "2026-11-02T00:03:33+00:00"
    },
    {
      "combined_score": null,
      "content_id": "fd5cd03b3f74",
      "creator_id": "khoi",
      "guess": null,
      "label": null,
      "model_score": 0.1727,
      "status": "decided",
      "style_score": null,
      "timestamp": "2026-11-02T00:10:20+00:00"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:*I asked Claude to help me build appeal in app.py
- *What came back:*A route that validates content_id and reasoning with 400s, reads creator_id off the original decision entry, calls log_appeal, and returns the new entry's timestamp as recorded_at.
- *What I changed:*I add when entries_for find nothing, it return 404

**Moment 2**

- *What I asked for:*I asked for help wording the "unsure" label and for the reasoning paragraph explaining it, after writing the three labels' ranges myself.
- *What came back:*A draft label that put the uncertainty on the system ("we couldn't tell") rather than the writer, stated that nothing happens to the piece, and ended with something the writer could do.
- *What I changed:*I add an offer to appeal if they think they are wrong.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 8 per minute, 400 per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->
     A real writer can't send more than 3 or 4 submit per minutes. Also, GPT-2 runs will also
     take a few seconds. I put 8 in case someone is really good. 40 per day is more than enough for a writing.


**What a caller counts as:** <!-- per address, or per creator_id? They fail
     differently — one script can look like a thousand callers, and one household
     can look like one. -->
     per creator_id. `rate_limit_key()` in `app.py`
     uses the creator_id from the request, and only falls back to the caller's
     address when there's no usable creator_id (missing, empty, or not a string).

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```
15 submissions as 'flood_tester' against http://127.0.0.1:5000
The first one is slow while the model loads.

  [ 1/15] 200
  [ 2/15] 200
  [ 3/15] 200
  [ 4/15] 200
  [ 5/15] 200
  [ 6/15] 200
  [ 7/15] 200
  [ 8/15] 200
  [ 9/15] 429
  [10/15] 429
  [11/15] 429
  [12/15] 429
  [13/15] 429
  [14/15] 429
  [15/15] 429

============================================================
200 200 200 200 200 200 200 200 429 429 429 429 429 429 429
============================================================
```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json
{"timestamp": "2026-11-02T00:03:33+00:00", "content_id": "c3c975928dc1", "creator_id": "khoi", "guess": null, "model_score": 0.1727, "style_score": null, "combined_score": null, "label": null, "status": "decided"}
{"timestamp": "2026-11-02T00:10:20+00:00", "content_id": "fd5cd03b3f74", "creator_id": "khoi", "guess": null, "model_score": 0.1727, "style_score": null, "combined_score": null, "label": null, "status": "decided"}
{"timestamp": "2026-11-02T00:50:59+00:00", "content_id": "6f274b1c4d99", "creator_id": "khoi", "guess": null, "model_score": 0.1727, "style_score": 0.5, "combined_score": 0.23816, "label": null, "status": "decided"}
{"timestamp": "2026-11-02T00:51:46+00:00", "content_id": "6f274b1c4d99", "creator_id": "khoi", "event": "appeal", "status": "under_review", "reasoning": "I wrote this myself on a rainy afternoon and have the drafts to show it."}
{"timestamp": "2026-11-02T00:51:46+00:00", "content_id": "6f274b1c4d99", "creator_id": "khoi", "event": "appeal", "status": "under_review", "reasoning": "I wrote this myself on a rainy afternoon and have the drafts to show it."}
{"timestamp": "2026-11-08T01:24:34+00:00", "content_id": "629986ebcbdf", "creator_id": "flood_tester", "guess": null, "model_score": 0.2587, "style_score": 0.5, "combined_score": 0.30696, "label": null, "status": "decided"}
{"timestamp": "2026-11-08T01:24:34+00:00", "content_id": "ad79a21acc00", "creator_id": "flood_tester", "guess": null, "model_score": 0.2587, "style_score": 0.5, "combined_score": 0.30696, "label": null, "status": "decided"}
{"timestamp": "2026-11-08T01:24:34+00:00", "content_id": "d72acfac5a33", "creator_id": "flood_tester", "guess": null, "model_score": 0.2587, "style_score": 0.5, "combined_score": 0.30696, "label": null, "status": "decided"}
{"timestamp": "2026-11-08T01:24:35+00:00", "content_id": "415e29307dba", "creator_id": "flood_tester", "guess": null, "model_score": 0.2587, "style_score": 0.5, "combined_score": 0.30696, "label": null, "status": "decided"}
{"timestamp": "2026-11-08T01:24:35+00:00", "content_id": "42f2ca93ae74", "creator_id": "flood_tester", "guess": null, "model_score": 0.2587, "style_score": 0.5, "combined_score": 0.30696, "label": null, "status": "decided"}
```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:
{"timestamp": "2026-11-08T01:36:39+00:00", "content_id": "d70e5352ef20", "creator_id": "attacker_FP07", "guess": "ai", "model_score": 0.8816, "style_score": 0.396, "combined_score": 0.7844800000000002, "label": "We think this was probably written with an AI tool. If you wrote it yourself, you can appeal and a person will review it.", "status": "decided"}



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Writing flagged high-confidence AI | at most 2 of 10 | 1/10 | 1/10 | 1/10 | MET |
| 2. Gap between clearly-AI and clearly-human scores | ≥ 0.6 | avg 0.32 | avg 0.32 | avg 0.32  | MISSED |
| 3. Every score gets a label | 7 of 7 | 7/7 | 7/7 | 7/7 | MET |
| 4. Appeal changes status and appears in log | 5 of 5 | 5/5 changed, 5/5 logged | same | same | MET |
| 5. Missing text returns 400, no crash, no log entry | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:
from `results/run_2026-11-07_2119_before.md` ("my own writing", Trial 1), produced by `run_eval.py::main`, `app.py::submit`.
```json
{
  "status": 200,
  "guess": "ai",
  "confidence": 0.70418,
  "model_score": 0.7305,
  "style_score": 0.5989,
  "label": "We think this was probably written with an AI tool. If you wrote it yourself, you can appeal and a person will review it.",
  "error": null,
  "message": null,
  "sent": "Anthony looked at the picture some time, slowly pursing up his lips, a"
}
```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**

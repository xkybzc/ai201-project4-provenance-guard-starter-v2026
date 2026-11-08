# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-07 20:36
- Auto-marked BROKE (5xx, crash, no response): **1**
- Left for you to judge: **55**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `29b68beef1cc` | human | 0.222 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `15f72a874543` | unsure | 0.503 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `d1f720ade565` | unsure | 0.586 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `693fc37a5a5a` | unsure | 0.580 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `03d1e65bccfd` | human | 0.287 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `289c1cf734cc` | unsure | 0.474 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `4b550225fd74` | unsure | 0.569 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `326ec1f26954` | human | 0.296 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `ab4b3f2e1856` | unsure | 0.607 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `85e877fc1009` | ai | 0.887 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `a2a690b33a1a` | unsure | 0.549 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `ba7434b0334b` | ai | 0.680 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `21c7abda4f07` | ai | 0.714 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `db549f5449f3` | ai | 0.726 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `aa357ee9038a` | ai | 0.750 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `2b6037245db2` | ai | 0.749 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `d70e5352ef20` | ai | 0.784 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `d54a844125b3` | unsure | 0.358 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `5602f6be218d` | unsure | 0.382 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `b16c58b65b72` | human | 0.190 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `c67de91dafb2` | unsure | 0.541 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `fb5891ee395f` | unsure | 0.460 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `12aea08e8ff5` | unsure | 0.612 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `f1f4300b6aba` | unsure | 0.498 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `c072609280d5` | human | 0.100 |  |
| MF04 | malformed | text is only punctuation | 200 | `8176ddf8e3e9` | human | 0.109 |  |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — |  |
| MF06 | malformed | text is emoji only | 200 | `4e139ed8828f` | ai | 0.898 |  |
| MF07 | malformed | text is right-to-left script | 200 | `111f8cb30700` | ai | 0.825 |  |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `c13dafc738c3` | human | 0.292 |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 200 | `d77769b2a1bd` | human | 0.139 |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4aea8418571c` | human | 0.123 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0d52fc02f0a8` | human | 0.123 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `29c9874d5f26` | human | 0.123 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b62bab4bd718` | human | 0.123 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f6e165b8fe9e` | human | 0.123 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1beb04cc602c` | human | 0.123 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `653be855b534` | human | 0.123 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `671a5588aea3` | human | 0.123 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 1 | 19 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "29b68beef1cc",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.22188000000000002,
  "model_score": 0.1635,
  "style_score": 0.4554,
  "label": "We think this was written by a person. No action is needed.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "15f72a874543",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.5028000000000001,
  "model_score": 0.5943,
  "style_score": 0.1368,
  "label": "We couldn't tell whether this was written by a person or with an AI tool. Nothing happens to your piece because of this. If you'd like, you can tell us about how you wrote it.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "d1f720ade565",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.58646,
  "model_score": 0.6662,
  "style_score": 0.2675,
  "label": "We couldn't tell whether this was written by a person or with an AI tool. Nothing happens to your piece because of this. If you'd like, you can tell us about how you wrote it.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "693fc37a5a5a",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.58018,
  "model_score": 0.6114,
  "style_score": 0.4553,
  "label": "We couldn't tell whether this was written by a person or with an AI tool. Nothing happens to your piece because of this. If you'd like, you can tell us about how you wrote it.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "03d1e65bccfd",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.28654,
  "model_score": 0.3212,
  "style_score": 0.1479,
  "label": "We think this was written by a person. No action is needed.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "289c1cf734cc",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.47412,
  "model_score": 0.5727,
  "style_score": 0.0798,
  "label": "We couldn't tell whether this was written by a person or with an AI tool. Nothing happens to your piece because of this. If you'd like, you can tell us about how you wrote it.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "4b550225fd74",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.56896,
  "model_score": 0.5862,
  "style_score": 0.5,
  "label": "We couldn't tell whether this was written by a person or with an AI tool. Nothing happens to your piece because of this. If you'd like, you can tell us about how you wrote it.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "326ec1f26954",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.29616,
  "model_score": 0.2452,
  "style_score": 0.5,
  "label": "We think this was written by a person. No action is needed.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "ab4b3f2e1856",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.6069200000000001,
  "model_score": 0.7042,
  "style_score": 0.2178,
  "label": "We couldn't tell whether this was written by a person or with an AI tool. Nothing happens to your piece because of this. If you'd like, you can tell us about how you wrote it.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "85e877fc1009",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8865000000000001,
  "model_score": 0.9792,
  "style_score": 0.5157,
  "label": "We think this was probably written with an AI tool. If you wrote it yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "a2a690b33a1a",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5492400000000001,
  "model_score": 0.6175,
  "style_score": 0.2762,
  "label": "We couldn't tell whether this was written by a person or with an AI tool. Nothing happens to your piece because of this. If you'd like, you can tell us about how you wrote it.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "ba7434b0334b",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.6802600000000001,
  "model_score": 0.7387,
  "style_score": 0.4465,
  "label": "We think this was probably written with an AI tool. If you wrote it yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "21c7abda4f07",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.7135200000000002,
  "model_score": 0.8051,
  "style_score": 0.3472,
  "label": "We think this was probably written with an AI tool. If you wrote it yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "db549f5449f3",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.72562,
  "model_score": 0.8329,
  "style_score": 0.2965,
  "label": "We think this was probably written with an AI tool. If you wrote it yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "aa357ee9038a",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.7501200000000001,
  "model_score": 0.8005,
  "style_score": 0.5486,
  "label": "We think this was probably written with an AI tool. If you wrote it yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "2b6037245db2",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.7492599999999999,
  "model_score": 0.8814,
  "style_score": 0.2207,
  "label": "We think this was probably written with an AI tool. If you wrote it yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "d70e5352ef20",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.7844800000000002,
  "model_score": 0.8816,
  "style_score": 0.396,
  "label": "We think this was probably written with an AI tool. If you wrote it yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "d54a844125b3",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.35784000000000005,
  "model_score": 0.3223,
  "style_score": 0.5,
  "label": "We couldn't tell whether this was written by a person or with an AI tool. Nothing happens to your piece because of this. If you'd like, you can tell us about how you wrote it.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "5602f6be218d",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.38222000000000006,
  "model_score": 0.4625,
  "style_score": 0.0611,
  "label": "We couldn't tell whether this was written by a person or with an AI tool. Nothing happens to your piece because of this. If you'd like, you can tell us about how you wrote it.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "b16c58b65b72",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.1899,
  "model_score": 0.2044,
  "style_score": 0.1319,
  "label": "We think this was written by a person. No action is needed.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "c67de91dafb2",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5413800000000001,
  "model_score": 0.5943,
  "style_score": 0.3297,
  "label": "We couldn't tell whether this was written by a person or with an AI tool. Nothing happens to your piece because of this. If you'd like, you can tell us about how you wrote it.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "fb5891ee395f",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.46004,
  "model_score": 0.4998,
  "style_score": 0.301,
  "label": "We couldn't tell whether this was written by a person or with an AI tool. Nothing happens to your piece because of this. If you'd like, you can tell us about how you wrote it.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "12aea08e8ff5",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.61208,
  "model_score": 0.6401,
  "style_score": 0.5,
  "label": "We couldn't tell whether this was written by a person or with an AI tool. Nothing happens to your piece because of this. If you'd like, you can tell us about how you wrote it.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "f1f4300b6aba",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.49812000000000006,
  "model_score": 0.5583,
  "style_score": 0.2574,
  "label": "We couldn't tell whether this was written by a person or with an AI tool. Nothing happens to your piece because of this. If you'd like, you can tell us about how you wrote it.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "c072609280d5",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.1,
  "model_score": 0.0,
  "style_score": 0.5,
  "label": "We think this was written by a person. No action is needed.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "8176ddf8e3e9",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.10896,
  "model_score": 0.0112,
  "style_score": 0.5,
  "label": "We think this was written by a person. No action is needed.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "4e139ed8828f",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.89752,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "We think this was probably written with an AI tool. If you wrote it yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "111f8cb30700",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.82512,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "We think this was probably written with an AI tool. If you wrote it yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "c13dafc738c3",
  "creator_id": null,
  "guess": "human",
  "confidence": 0.29159999999999997,
  "model_score": 0.2395,
  "style_score": 0.5,
  "label": "We think this was written by a person. No action is needed.",
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 200,
  "content_id": "d77769b2a1bd",
  "creator_id": {
    "id": "x"
  },
  "guess": "human",
  "confidence": 0.13936,
  "model_score": 0.0492,
  "style_score": 0.5,
  "label": "We think this was written by a person. No action is needed.",
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "4aea8418571c",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.12296000000000001,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was written by a person. No action is needed.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "0d52fc02f0a8",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.12296000000000001,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was written by a person. No action is needed.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "29c9874d5f26",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.12296000000000001,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was written by a person. No action is needed.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "b62bab4bd718",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.12296000000000001,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was written by a person. No action is needed.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "f6e165b8fe9e",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.12296000000000001,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was written by a person. No action is needed.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "1beb04cc602c",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.12296000000000001,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was written by a person. No action is needed.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "653be855b534",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.12296000000000001,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was written by a person. No action is needed.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "671a5588aea3",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.12296000000000001,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was written by a person. No action is needed.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

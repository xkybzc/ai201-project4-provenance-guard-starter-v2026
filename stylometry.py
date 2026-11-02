"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]

def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())

MIN_WORDS = 20
MIN_SENTENCES = 3
TTR_WINDOW = 100
SPREAD_HUMAN_CV = 0.6
TTR_LOW, TTR_HIGH = 0.45, 0.80
PUNCT_LOW, PUNCT_HIGH = 0.05, 0.25
WEIGHTS = {"spread": 0.5, "ttr": 0.3, "punct": 0.2}
NEUTRAL = 0.5
_PUNCT = re.compile(r"[,;:.!?\u2014\u2013\-()\"]")

def _clamp(x: float) -> float:
    return max(0.0, min(1.0, x))

def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies: stdev / mean of words per sentence.

    Scale: 0.0 means every sentence is the same length. Around 0.6 or more is
    lumpy, human-looking variation. HIGH = more human.

    Edge case: fewer than two sentences has no spread, and `stdev` would raise,
    so this returns 0.0. That reads as "perfectly even", which is why
    style_signal() refuses to score texts this short instead of trusting it.
    """
    lengths = [len(words(s)) for s in sentences(text)]
    if len(lengths) < 2:
        return 0.0
    mean = statistics.mean(lengths)
    if mean == 0:
        return 0.0
    return statistics.pstdev(lengths) / mean

def type_token_ratio(text: str) -> float:
    """
    Unique words over total words, on the first TTR_WINDOW words.
    Returns a float between 0 and 1. HIGH = more varied vocabulary = more human.
    Measured on a fixed window because the ratio falls as text gets longer;
    otherwise a long text and a short one aren't comparable.
    """
    w = words(text)[:TTR_WINDOW]
    if not w:
        return 0.0
    return len(set(w)) / len(w)
 
 
def punctuation_density(text: str) -> float:
    """
    Punctuation marks per word (see _PUNCT for what counts).

    HIGH = more punctuation = treated as more AI-like. That direction is a
    guess, not a fact: casual human writing can be full of commas, dashes and
    exclamation marks too. Test it before you trust it.
    """
    w = words(text)
    if not w:
        return 0.0
    return len(_PUNCT.findall(text)) / len(w)

def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. **Higher means more likely AI.**
    Each raw measure is turned into an "AI-likeness" from 0.0 to 1.0, so they're
    on the same scale and the same direction as detector.model_signal:
        spread  : LOW spread        -> more AI   (flipped)
        ttr     : LOW variety       -> more AI   (flipped)
        punct   : HIGH density      -> more AI   (not flipped)
    Then a weighted average (WEIGHTS above). Returns NEUTRAL (0.5) when there is
    too little text to measure.
    """
    s = sentences(text)
    w = words(text)
    if len(w) < MIN_WORDS or len(s) < MIN_SENTENCES:
        return NEUTRAL
    spread_ai = 1.0 - _clamp(sentence_length_spread(text) / SPREAD_HUMAN_CV)
    ttr_ai = _clamp((TTR_HIGH - type_token_ratio(text)) / (TTR_HIGH - TTR_LOW))
    punct_ai = _clamp((punctuation_density(text) - PUNCT_LOW) / (PUNCT_HIGH - PUNCT_LOW))
    score = (
        WEIGHTS["spread"] * spread_ai
        + WEIGHTS["ttr"] * ttr_ai
        + WEIGHTS["punct"] * punct_ai
    )
    return round(_clamp(score), 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
    print("\nAll zeros? These are stubs — Milestone 4 is where you build them.")

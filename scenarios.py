"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

MY_WRITING = [
    "Charm is a very peculiar thing; hundreds of young women, some of them more beautiful than Virginia Revel, might have said “Hullo, Bill,” with exactly the same intonation, and yet have produced no effect whatever. But those two simple words, uttered by Virginia, had the most intoxicating effect upon Bill.",
    "Virginia Revel was just twenty-seven. She was tall and of an exquisite slimness—indeed, a poem might have been written to her slimness, it was so exquisitely proportioned.",
    "Her hair was of real bronze, with the greenish tint in its gold; she had a determined little chin, a lovely nose, slanting blue eyes that showed a gleam of deepest cornflower between the half-closed lids, and a delicious and quite indescribable mouth that tilted ever so slightly at one corner in what is known as “the signature of Venus.”",
    "Bill Eversleigh was an extremely nice lad. He was a good cricketer and a scratch golfer, he had pleasant manners, and an amiable disposition, but his position in the Foreign Office had been gained, not by brains, but by good connections. For the work he had to do he was quite suitable. He was more or less George’s dog. He did no responsible or brainy work.",
    "He retraced his steps back to the Blitz. Just as he was crossing the road, a man jostled against him, nearly making him lose his balance. They both recovered themselves, and the man muttered an apology, his eyes scanning Anthony’s face narrowly. He was a short, thickset man of the working classes, with something foreign in his appearance.",
    "Anthony went on into the hotel, wondering, as he did so, what had inspired that searching glance. Nothing in it probably. The deep tan of his face was somewhat unusual looking amongst these pallid Londoners and it had attracted the fellow’s attention.",
    "He went up to his room and, led by a sudden impulse, crossed to the looking-glass and stood studying his face in it. Of the few friends of the old days—just a chosen few—was it likely that any of them would recognize him now if they were to meet him face to face? He shook his head slowly.",
    "When he had left London he had been just eighteen—a fair, slightly chubby boy, with a misleading seraphic expression. Small chance that the boy would be recognized in the lean, brown-faced man with the quizzical expression.",
    "Anthony looked at the picture some time, slowly pursing up his lips, as though to whistle. Then he tore out the whole page, folded it up and put it in his pocket. He went upstairs again, unlocked his suit-case and took out the packet of letters. He took out the folded page from his pocket and slipped it under the string that held them together.",
    "Looking at his watch, Anthony discovered that it was nearly nine o’clock, and he decided to dine where he was. He did not anticipate any more surprise visits, but he felt that it was up to him to be on his guard. He had no intention of allowing his suit-case to be rifled whilst he was downstairs in the Grill Room. ",
]

CLEARLY_AI = [
    "Time management is an essential skill for students at every level. By "
    "prioritizing tasks, setting clear goals, and creating a structured "
    "schedule, students can reduce stress and improve their academic "
    "performance. Additionally, breaking large assignments into smaller, "
    "manageable steps can make them feel less overwhelming. Ultimately, "
    "developing strong time management habits early on can lead to long-term "
    "success both in school and in future careers.",
 
    "Climate change is one of the most pressing challenges facing the world "
    "today. Rising global temperatures are leading to more frequent extreme "
    "weather events, melting ice caps, and rising sea levels. Addressing this "
    "issue requires a combination of individual action, corporate "
    "responsibility, and government policy. By working together, communities "
    "around the world can reduce emissions and build a more sustainable future "
    "for generations to come.",
 
    "Reading offers numerous benefits for both personal and professional "
    "growth. It expands vocabulary, improves concentration, and enhances "
    "critical thinking skills. Furthermore, reading exposes individuals to new "
    "perspectives and ideas, fostering empathy and understanding. Whether it is "
    "fiction or nonfiction, making reading a regular habit can significantly "
    "enrich one's life and contribute to lifelong learning.",
 
    "Remote work has transformed the modern workplace in significant ways. "
    "Employees benefit from greater flexibility, reduced commuting time, and an "
    "improved work-life balance. However, remote work also presents challenges, "
    "such as feelings of isolation and difficulties with communication. To "
    "succeed in a remote environment, it is important to establish a dedicated "
    "workspace, maintain regular communication with colleagues, and set clear "
    "boundaries between work and personal time.",
 
    "Exercise plays a crucial role in maintaining overall health and "
    "well-being. Regular physical activity strengthens the heart, improves "
    "mood, and boosts energy levels. In addition, exercise can help reduce the "
    "risk of chronic diseases such as diabetes and high blood pressure. "
    "Incorporating even a small amount of movement into your daily routine, "
    "such as walking or stretching, can make a meaningful difference over time.",
]

ODD_INPUTS = [
    # Very repetitive, highly predictable text: should push signal one high.
    "The cat sat on the mat. The cat sat on the mat. The cat sat on the mat. "
    "The cat sat on the mat. The cat sat on the mat. The cat sat on the mat.",
 
    # A list with almost no sentence structure: one 'sentence' to the splitter.
    "eggs milk bread butter apples rice chicken onions garlic tomatoes pasta "
    "cheese yogurt spinach carrots coffee tea sugar flour salt pepper oil",
 
    # Casual, choppy, typo-filled human-style text.
    "ok so i missed the bus AGAIN. third time this week lol. ran the whole way "
    "and still got there late, teacher just gave me the look. whatever. "
    "tomorrow im leaving at 7 no excuses. probably.",
]

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        # ⚠️ PUT YOUR OWN WRITING HERE. Not AI text, not a sample from the web —
        # things you actually wrote. This is the criterion that matters most and
        # it's meaningless with someone else's prose.
        "texts": MY_WRITING,

    },
    {
        "name": "label coverage",
        "criterion": 2,
        # Inputs spread across your score range, so you can check all three
        # labels are actually reachable.
        "texts": CLEARLY_AI,
        
    },
    {
        "name": "label coverage",
        "criterion": 3,
        "texts": CLEARLY_AI[:2] + MY_WRITING[:2] + ODD_INPUTS,
    },
    {
        "name": "missing text",
        "criterion": 5,
        "bodies": [
            {"creator_id": "eval_bad_missing"},               # no text field
            {"text": None, "creator_id": "eval_bad_null"},    # text is null
            {"text": "", "creator_id": "eval_bad_empty"},     # empty string
            {"text": "     ", "creator_id": "eval_bad_space"},  # only spaces
            {},                                                # empty body
        ],
    },
    # A bad-input criterion looks like this. Uncomment and adjust if that's one
    # of your five — these are raw request bodies, sent exactly as written.
    #
    # {
    #     "name": "bad input",
    #     "criterion": 3,
    #     "bodies": [
    #         {"text": "", "creator_id": "eval_bad_empty"},
    #         {"creator_id": "eval_bad_missing"},          # no text field at all
    #         {"text": "word " * 50000, "creator_id": "eval_bad_huge"},
    #         {"text": None, "creator_id": "eval_bad_null"},
    #     ],
    # },

    # TODO: add what your remaining criteria need.
    #
    # A criterion about the appeal path can't be tested by sending text alone;
    # it needs a submission first and then an appeal against the content_id
    # that came back. You'll need to test that one by hand, or extend this file
    # and run_eval.py to do it. Saying which you did is part of the write-up.
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems

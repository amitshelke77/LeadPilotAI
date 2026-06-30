import re


BAD_WORDS = [

    "home",
    "manufacturer",
    "manufacturers",
    "supplier",
    "suppliers",
    "products",
    "plastic",
    "bags",
    "part",
    "parts",
    "top",
    "company",
    "companies",
    "india",
    "pune",
    "maharashtra",
]


def normalize_company_name(name: str):

    if not name:
        return None

    name = name.strip()

    separators = [

        "|",
        "—",
        "-",

    ]

    pieces = [name]

    for sep in separators:

        new = []

        for part in pieces:

            new.extend(part.split(sep))

        pieces = new

    candidates = []

    for part in pieces:

        part = part.strip()

        if len(part) < 3:
            continue

        words = part.lower().split()

        bad = sum(word in BAD_WORDS for word in words)

        score = len(words) - bad

        candidates.append((score, part))

    if not candidates:
        return None

    candidates.sort(reverse=True)

    best = candidates[0][1]

    # Remove trailing locations
    best = re.sub(
        r"\b(Pune|India|Maharashtra)\b",
        "",
        best,
        flags=re.I,
    )

    best = re.sub(r"\s+", " ", best)

    return best.strip(" ,-")
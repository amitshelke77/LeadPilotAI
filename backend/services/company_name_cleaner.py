import re


INVALID_WORDS = {
    "top",
    "best",
    "list",
    "directory",
    "blog",
    "yellowpages",
    "justdial",
    "indiamart",
    "tradeindia",
    "easyleadz",
    "findingmfg",
}


LOCATION_WORDS = {
    "pune",
    "maharashtra",
    "india",
}


def generate_candidates(title: str):

    title = title.replace("—", "-")
    title = title.replace("|", "-")

    candidates = []

    for part in re.split(r"-", title):

        part = part.strip()

        if part:
            candidates.append(part)

    return candidates


def score_candidate(text: str):

    lower = text.lower()

    score = 100

    for word in INVALID_WORDS:
        if word in lower:
            score -= 80

    for word in LOCATION_WORDS:
        if word in lower:
            score -= 20

    if len(text.split()) <= 1:
        score -= 40

    if len(text) < 4:
        score -= 50

    return score


def clean_company_name(title: str):

    if not title:
        return None

    candidates = generate_candidates(title)

    if not candidates:
        return None

    best = max(candidates, key=score_candidate)

    if score_candidate(best) <= 0:
        return None

    return best.strip()
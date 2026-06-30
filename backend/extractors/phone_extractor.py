import re
import requests

from backend.enrichers.evidence import Evidence
from backend.normalizers.phone_normalizer import normalize_phone


PHONE_REGEXES = [
    r"\+91[\s\-]?\d{10}",
    r"\+91[\s\-]?\d{5}[\s\-]?\d{5}",
    r"\b0\d{10}\b",
    r"\b\d{10}\b",
    r"\(\d{3,5}\)\s?\d+",
]


def extract_phones(url: str):
    """
    Extract phone numbers from a webpage.

    Returns:
        list[Evidence]
    """

    evidence = []

    try:

        response = requests.get(
            url,
            timeout=20,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
        )

        html = response.text

        phones = set()

        for regex in PHONE_REGEXES:

            matches = re.findall(regex, html)

            phones.update(matches)

        for phone in phones:

            normalized = normalize_phone(phone)

            if not normalized:
                continue

            evidence.append(
                Evidence(
                    field="phone",
                    value=normalized,
                    source="html",
                    confidence=0.80,
                )
            )

    except Exception:
        pass

    return evidence
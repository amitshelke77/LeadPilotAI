import re
import requests


PHONE_REGEXES = [
    r"\+91[\s\-]?\d{10}",
    r"\+91[\s\-]?\d{5}[\s\-]?\d{5}",
    r"\b0\d{10}\b",
    r"\b\d{10}\b",
    r"\(\d{3,5}\)\s?\d+",
]


def extract_phones(url: str):

    phones = set()

    try:

        response = requests.get(
            url,
            timeout=20,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
        )

        html = response.text

        for regex in PHONE_REGEXES:

            matches = re.findall(regex, html)

            for phone in matches:

                phone = phone.strip()

                if len(phone) >= 10:
                    phones.add(phone)

    except Exception:
        pass

    return sorted(phones)
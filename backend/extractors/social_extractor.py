import requests
from bs4 import BeautifulSoup

from backend.enrichers.evidence import Evidence


SOCIAL_DOMAINS = {
    "linkedin.com": "linkedin",
    "facebook.com": "facebook",
    "instagram.com": "instagram",
    "twitter.com": "twitter",
    "x.com": "twitter",
    "youtube.com": "youtube",
    "wa.me": "whatsapp",
    "t.me": "telegram",
}


def extract_social_links(url: str):

    evidence = []

    try:

        response = requests.get(
            url,
            timeout=15,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 Chrome/137.0 Safari/537.36"
                )
            },
        )

    except Exception:
        return evidence

    soup = BeautifulSoup(response.text, "html.parser")

    found = set()

    for tag in soup.find_all("a", href=True):

        href = tag["href"].strip()

        for domain, field in SOCIAL_DOMAINS.items():

            if domain in href.lower():

                if href not in found:

                    found.add(href)

                    evidence.append(
                        Evidence(
                            field=field,
                            value=href,
                            source="html",
                            confidence=0.95,
                        )
                    )

    return evidence
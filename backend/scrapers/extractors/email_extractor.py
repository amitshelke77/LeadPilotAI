import re
import requests

from bs4 import BeautifulSoup

from backend.enrichers.evidence import Evidence
from backend.normalizers.email_normalizer import normalize_email


EMAIL_REGEX = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"


def extract_emails(url: str):
    """
    Extract email addresses from a website.

    Returns:
        list[Evidence]
    """

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    pages = [url]

    evidence = []

    try:

        response = requests.get(
            url,
            headers=headers,
            timeout=15,
        )

        soup = BeautifulSoup(response.text, "html.parser")

        for link in soup.find_all("a", href=True):

            href = link["href"]

            if "contact" in href.lower():

                if href.startswith("http"):
                    pages.append(href)

                else:
                    pages.append(
                        url.rstrip("/") + "/" + href.lstrip("/")
                    )

        normalized_emails = set()

        for page in pages:

            try:

                r = requests.get(
                    page,
                    headers=headers,
                    timeout=15,
                )

                matches = re.findall(EMAIL_REGEX, r.text)

                for email in matches:

                    normalized = normalize_email(email)

                    if normalized:
                        normalized_emails.add(normalized)

            except Exception:
                continue

        for email in sorted(normalized_emails):

            evidence.append(
                Evidence(
                    field="email",
                    value=email,
                    source="html",
                    confidence=0.90,
                )
            )

    except Exception:
        pass

    return evidence
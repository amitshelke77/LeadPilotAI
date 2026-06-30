import re
import requests
from bs4 import BeautifulSoup

EMAIL_REGEX = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"


def extract_emails(url: str):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    pages = [url]

    try:
        response = requests.get(url, headers=headers, timeout=15)

        soup = BeautifulSoup(response.text, "html.parser")

        for link in soup.find_all("a", href=True):
            href = link["href"]

            if "contact" in href.lower():
                if href.startswith("http"):
                    pages.append(href)
                else:
                    pages.append(url.rstrip("/") + "/" + href.lstrip("/"))

        emails = set()

        for page in pages:
            try:
                r = requests.get(page, headers=headers, timeout=15)
                emails.update(re.findall(EMAIL_REGEX, r.text))
            except Exception:
                pass

        return sorted(emails)

    except Exception:
        return []
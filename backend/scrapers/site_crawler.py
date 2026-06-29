from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup


KEYWORDS = [
    "contact",
    "about",
    "team",
    "support",
    "company",
    "careers",
    "services",
]

SKIP_EXTENSIONS = (
    ".pdf",
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".webp",
    ".svg",
    ".zip",
    ".rar",
    ".doc",
    ".docx",
    ".xls",
    ".xlsx",
    ".ppt",
    ".pptx",
    ".mp4",
    ".mp3",
)

SKIP_DOMAINS = (
    "facebook.com",
    "instagram.com",
    "linkedin.com",
    "youtube.com",
    "twitter.com",
)


def crawl_site(homepage: str, max_pages: int = 8):

    pages = set()

    try:

        response = requests.get(
            homepage,
            timeout=15,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
        )

        soup = BeautifulSoup(response.text, "html.parser")

        domain = urlparse(homepage).netloc

        for link in soup.find_all("a", href=True):

            href = link["href"]

            url = urljoin(homepage, href)

            parsed = urlparse(url)

            if parsed.netloc != domain:
                continue

            if any(ext in url.lower() for ext in SKIP_EXTENSIONS):
                continue

            if any(d in url.lower() for d in SKIP_DOMAINS):
                continue

            text = link.get_text(" ", strip=True).lower()

            score = 0

            for keyword in KEYWORDS:

                if keyword in url.lower():
                    score += 3

                if keyword in text:
                    score += 2

            pages.add((score, url))

    except Exception:

        return [homepage]

    ranked = sorted(
        pages,
        key=lambda x: x[0],
        reverse=True,
    )

    results = []

    for _, url in ranked:

        if url not in results:
            results.append(url)

        if len(results) >= max_pages:
            break

    if homepage not in results:
        results.insert(0, homepage)

    return results
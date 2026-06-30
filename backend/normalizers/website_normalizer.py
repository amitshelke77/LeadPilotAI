from urllib.parse import urlparse


def normalize_website(url: str) -> str | None:

    if not url:
        return None

    url = url.strip()

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    parsed = urlparse(url)

    domain = parsed.netloc.lower()

    if domain.startswith("www."):
        domain = domain[4:]

    normalized = f"https://{domain}"

    return normalized
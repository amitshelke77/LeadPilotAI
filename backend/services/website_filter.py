BLOCKED_DOMAINS = {
    "justdial.com",
    "indiamart.com",
    "tradeindia.com",
    "easyleadz.com",
    "facebook.com",
    "linkedin.com",
    "instagram.com",
    "youtube.com",
    "twitter.com",
    "x.com",
    "exportersindia.com",
    "yellowpages.com",
    "sulekha.com",
    "amazon.in",
    "flipkart.com",
}

BLOCKED_KEYWORDS = {
    "top",
    "list",
    "directory",
    "blog",
    "manufacturer list",
}


def is_valid_company_website(url: str, title: str = "") -> bool:

    url = url.lower()
    title = title.lower()

    for domain in BLOCKED_DOMAINS:
        if domain in url:
            return False

    for keyword in BLOCKED_KEYWORDS:
        if keyword in title:
            return False

    return True
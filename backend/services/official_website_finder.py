from ddgs import DDGS


BLOCKED_DOMAINS = {
    "justdial.com",
    "indiamart.com",
    "tradeindia.com",
    "yellowpages.com",
    "webindia123.com",
    "easyleadz.com",
}


def find_official_website(company_name: str):
    """
    Search DuckDuckGo for the company's official website.

    Returns:
        str | None
    """

    query = f"{company_name} official website"

    try:

        with DDGS() as ddgs:

            results = ddgs.text(
                query,
                max_results=5,
            )

            for result in results:

                url = result.get("href") or result.get("url")

                if not url:
                    continue

                url_lower = url.lower()

                if any(domain in url_lower for domain in BLOCKED_DOMAINS):
                    continue

                return url

    except Exception as e:

        print(f"Official Website Finder Error: {e}")

    return None
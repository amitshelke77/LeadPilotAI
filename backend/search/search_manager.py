from backend.scrapers.search.web_search import search_company_websites


def search_companies(industry: str, location: str, limit: int = 10):
    """
    Main search entry point.

    In the future this manager will combine:
    - DDGS
    - Google Maps
    - Brave Search
    - Bing
    - Serper
    """

    results = []

    try:
        results.extend(
            search_company_websites(
                industry,
                location,
                limit,
            )
        )
    except Exception as e:
        print(f"DDGS Error: {e}")

    # Future Providers
    #
    # results.extend(search_google_maps(...))
    # results.extend(search_brave(...))
    # results.extend(search_bing(...))

    return remove_duplicates(results)


def remove_duplicates(results):

    unique = {}

    for item in results:

        website = item.get("Website", "").lower()

        if website not in unique:
            unique[website] = item

    return list(unique.values())
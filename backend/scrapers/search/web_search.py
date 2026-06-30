from ddgs import DDGS


def search_company_websites(
    industry: str,
    location: str,
    max_results: int = 20,
):
    """
    Search company websites using DDGS.
    """

    query = f"{industry} {location}"

    companies = []

    try:
        with DDGS() as ddgs:
            results = ddgs.text(
                query,
                max_results=max_results,
            )

            for result in results:
                companies.append(
                    {
                        "Company": result.get("title", ""),
                        "Website": result.get("href", ""),
                        "Source": "DDGS",
                    }
                )

    except Exception as e:
        print(f"Search Error: {e}")

    return companies
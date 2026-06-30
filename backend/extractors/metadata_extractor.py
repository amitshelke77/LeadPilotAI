import requests
from bs4 import BeautifulSoup


def extract_metadata(url: str):

    result = {
        "title": "",
        "description": "",
        "company_name": "",
    }

    try:

        response = requests.get(
            url,
            timeout=20,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
        )

        soup = BeautifulSoup(response.text, "html.parser")

        # HTML Title
        if soup.title:
            result["title"] = soup.title.get_text(strip=True)

        # Meta Description
        description = soup.find(
            "meta",
            attrs={"name": "description"},
        )

        if description:
            result["description"] = description.get(
                "content",
                "",
            )

        # OpenGraph Site Name
        og = soup.find(
            "meta",
            attrs={"property": "og:site_name"},
        )

        if og:
            result["company_name"] = og.get(
                "content",
                "",
            )

        # Fallback
        if not result["company_name"]:
            result["company_name"] = result["title"]

    except Exception as e:

        print(e)

    return result
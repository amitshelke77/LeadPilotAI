import requests


OVERPASS_URL = "https://overpass-api.de/api/interpreter"


def search_places(industry: str, location: str, limit: int = 50):
    """
    Search OpenStreetMap businesses using Overpass API.
    Returns a list of dictionaries.
    """

    query = f"""
    [out:json][timeout:25];

    area["name"="{location}"]->.searchArea;

    (
      node["name"]["shop"](area.searchArea);
      way["name"]["shop"](area.searchArea);
      relation["name"]["shop"](area.searchArea);
    );

    out center {limit};
    """

    try:
        response = requests.post(
            OVERPASS_URL,
            data=query,
            timeout=60,
        )

        response.raise_for_status()

        data = response.json()

        companies = []

        keyword = industry.lower()

        for element in data.get("elements", []):

            tags = element.get("tags", {})

            name = tags.get("name", "")

            if keyword not in name.lower():
                continue

            companies.append(
                {
                    "Company": name,
                    "Location": location,
                    "Website": tags.get("website", ""),
                    "Email": tags.get("email", ""),
                    "Phone": tags.get("phone", ""),
                }
            )

        return companies

    except Exception as e:
        print(e)
        return []
import pandas as pd

from backend.services.maps_search import search_places


def search_companies(industry, location, max_results):

    companies = search_places(
        industry,
        location,
        max_results,
    )

    if not companies:
        return pd.DataFrame(
            columns=[
                "Company",
                "Location",
                "Website",
                "Email",
                "Phone",
            ]
        )

    return pd.DataFrame(companies)
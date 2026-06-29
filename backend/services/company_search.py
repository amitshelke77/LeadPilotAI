import pandas as pd


def search_companies(industry, location, max_results):
    """
    Temporary dummy data.
    Next sprint we'll replace this with real Google/Maps search.
    """

    data = []

    for i in range(1, max_results + 1):
        data.append(
            {
                "Company": f"{industry} Company {i}",
                "Location": location,
                "Website": "",
                "Email": "",
                "Phone": "",
            }
        )

    return pd.DataFrame(data)
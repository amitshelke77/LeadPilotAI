import json
import requests

from bs4 import BeautifulSoup


VALID_TYPES = {

    "Organization",
    "Corporation",
    "LocalBusiness",
    "Manufacturer",
    "Store",
    "Business",

}


def has_valid_type(schema):

    types = schema.get("@type")

    if not types:
        return False

    if isinstance(types, str):
        return types in VALID_TYPES

    if isinstance(types, list):

        return any(t in VALID_TYPES for t in types)

    return False


def extract_jsonld(url):

    try:

        response = requests.get(

            url,

            timeout=15,

            headers={
                "User-Agent": "Mozilla/5.0"
            },

        )

    except Exception:

        return None

    soup = BeautifulSoup(response.text, "html.parser")

    scripts = soup.find_all(

        "script",

        type="application/ld+json",

    )

    for script in scripts:

        if not script.string:
            continue

        try:

            data = json.loads(script.string)

        except Exception:

            continue

        if isinstance(data, dict):

            if has_valid_type(data):
                return data

            # Support @graph
            graph = data.get("@graph")

            if isinstance(graph, list):

                for item in graph:

                    if isinstance(item, dict):

                        if has_valid_type(item):
                            return item

        elif isinstance(data, list):

            for item in data:

                if isinstance(item, dict):

                    if has_valid_type(item):
                        return item

    return None
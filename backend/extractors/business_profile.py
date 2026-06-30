from backend.extractors.jsonld_extractor import extract_jsonld


def extract_business_profile(url: str):

    profile = {
        "company": None,
        "description": None,
        "phone": None,
        "website": None,
        "logo": None,
        "address": None,
    }

    data = extract_jsonld(url)

    if not data:
        return profile

    profile["company"] = data.get("name")
    profile["description"] = data.get("description")
    profile["phone"] = data.get("telephone")
    profile["website"] = data.get("url")
    profile["logo"] = data.get("logo")

    address = data.get("address")

    if isinstance(address, dict):

        parts = []

        for field in (
            "streetAddress",
            "addressLocality",
            "addressRegion",
            "postalCode",
            "addressCountry",
        ):

            value = address.get(field)

            if value:
                parts.append(value)

        profile["address"] = ", ".join(parts)

    return profile
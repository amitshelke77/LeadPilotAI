from backend.enrichers.merge_engine import merge_evidence


def build_business_profile(evidence):

    merged = merge_evidence(evidence)

    profile = {
        "company": None,
        "website": None,
        "description": None,
        "logo": None,
        "phone": None,
        "emails": [],
        "address": None,
        "city": None,
        "state": None,
        "country": None,
        "linkedin": None,
        "facebook": None,
        "instagram": None,
        "youtube": None,
        "twitter": None,
        "whatsapp": None,
        "confidence": 0,
    }

    for field in profile.keys():

        if field in merged:

            profile[field] = merged[field]["value"]

    filled = 0

    total = len(profile) - 1

    for key, value in profile.items():

        if key == "confidence":
            continue

        if value not in (None, "", [], {}):

            filled += 1

    profile["confidence"] = round(filled / total * 100)

    return profile
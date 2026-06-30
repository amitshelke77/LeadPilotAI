from backend.scrapers.extractors.email_extractor import extract_emails
from backend.extractors.phone_extractor import extract_phones
from backend.extractors.metadata_extractor import extract_metadata
from backend.extractors.jsonld_extractor import extract_jsonld
from backend.extractors.social_extractor import extract_social_links


EXTRACTORS = [
    {
        "name": "emails",
        "function": extract_emails,
    },
    {
        "name": "phones",
        "function": extract_phones,
    },
    {
        "name": "metadata",
        "function": extract_metadata,
    },
    {
        "name": "jsonld",
        "function": extract_jsonld,
    },
    {
        "name": "social",
        "function": extract_social_links,
    },
]
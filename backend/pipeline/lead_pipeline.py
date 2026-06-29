from backend.scrapers.web_search import search_company_websites
from backend.scrapers.website_scraper import find_contact_page
from backend.services.email_extractor import extract_emails


def generate_leads(industry: str, location: str, limit: int = 10):
    """
    Complete lead generation pipeline.
    """

    results = search_company_websites(industry, location, limit)

    leads = []

    for company in results:

        website = company.get("Website", "")

        if not website:
            continue

        print(f"Processing: {website}")

        contact_page = find_contact_page(website)

        target = contact_page if contact_page else website

        emails = extract_emails(target)

        leads.append(
            {
                "Company": company.get("Company"),
                "Website": website,
                "Contact Page": contact_page,
                "Emails": ", ".join(emails),
            }
        )

    return leads
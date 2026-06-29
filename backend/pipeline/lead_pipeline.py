from backend.scrapers.web_search import search_company_websites
from backend.scrapers.site_crawler import crawl_site
from backend.services.email_extractor import extract_emails
from backend.services.website_filter import is_valid_company_website


def generate_leads(industry: str, location: str, limit: int = 10):

    companies = search_company_websites(industry, location, limit)

    leads = []

    for company in companies:

        website = company.get("Website", "")
        title = company.get("Company", "")

        if not website:
            continue

        if not is_valid_company_website(website, title):
            print(f"Skipped: {website}")
            continue

        print(f"\nProcessing: {website}")

        pages = crawl_site(website)

        all_emails = set()

        for page in pages:

            print(f"   Scanning: {page}")

            try:
                emails = extract_emails(page)
                all_emails.update(emails)
            except Exception:
                continue

        leads.append(
            {
                "Company": title,
                "Website": website,
                "Pages Crawled": len(pages),
                "Emails": ", ".join(sorted(all_emails)),
            }
        )

    return leads
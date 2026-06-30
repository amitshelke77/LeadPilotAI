from backend.search.search_manager import search_companies
from backend.scrapers.crawlers.site_crawler import crawl_site
from backend.scrapers.extractors.email_extractor import extract_emails
from backend.services.website_filter import is_valid_company_website
from backend.services.official_website_finder import find_official_website


def generate_leads(industry: str, location: str, limit: int = 10):

    companies = search_companies(industry, location, limit)

    leads = []

    for company in companies:

        website = company["Website"]

        # If the search result is a directory,
        # try finding the official company website.
        if not is_valid_company_website(website):

            official = find_official_website(company["Company"])

            if official:
                website = official
                company["Website"] = official
            else:
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
                "Company": company["Company"],
                "Website": website,
                "Pages Crawled": len(pages),
                "Emails": ", ".join(sorted(all_emails)),
            }
        )

    return leads
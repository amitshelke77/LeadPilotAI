from backend.scrapers.website_scraper import find_contact_page
from backend.services.email_extractor import extract_emails

url = "https://www.bharatplastic.org"

contact_page = find_contact_page(url)

print("Contact Page:", contact_page)

if contact_page:
    emails = extract_emails(contact_page)
else:
    emails = extract_emails(url)

print("Emails:", emails)
from backend.scrapers.website_scraper import find_contact_page

url = "https://www.bharatplastic.org"

contact = find_contact_page(url)

print(contact)
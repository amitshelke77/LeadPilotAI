from backend.scrapers.web_search import search_company_websites

results = search_company_websites(
    "Plastic Manufacturers",
    "Pune",
    10,
)

for company in results:
    print(company)
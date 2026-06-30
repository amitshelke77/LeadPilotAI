from backend.services.company_name_cleaner import (
    generate_candidates,
    clean_company_name,
)

tests = [
    "Plastic Bags Manufacturer | Sneha Polymer",
    "Advance Plastics Pune, Maharashtra, India | Home",
    "Top Plastic Manufacturing Companies in Pune | FindingMFG",
    "Bharat Plastic — Plastic Manufacturing Company in Pune",
    "Plastic Part Manufacturers in Pune - Shree Laxmi Engineering Works",
]

for test in tests:

    print("=" * 60)

    print("Original:")
    print(test)

    print()

    print("Candidates:")
    print(generate_candidates(test))

    print()

    print("Selected:")
    print(clean_company_name(test))

    print()
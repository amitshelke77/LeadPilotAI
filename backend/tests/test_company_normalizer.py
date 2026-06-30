from backend.normalizers.company_normalizer import normalize_company_name


examples = [

    "Plastic Bags Manufacturer | Sneha Polymer",

    "Advance Plastics Pune, Maharashtra, India | Home",

    "Top Plastic Manufacturing Companies in Pune | FindingMFG",

    "Bharat Plastic — Plastic Manufacturing Company in Pune",

    "Plastic Part Manufacturers in Pune - Shree Laxmi Engineering Works",

]

print()

for item in examples:

    print("=" * 60)

    print()

    print(item)

    print()

    print(normalize_company_name(item))
from backend.extractors.phone_extractor import extract_phones

url = "https://bharatplastic.org"

phones = extract_phones(url)

print()

print("=" * 60)

print(f"Found {len(phones)} phone evidence objects")

print("=" * 60)

for phone in phones:
    print(phone)
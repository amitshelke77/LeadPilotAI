from backend.extractors.phone_extractor import extract_phones

phones = extract_phones(
    "https://bharatplastic.org/"
)

print()

for phone in phones:
    print(phone)
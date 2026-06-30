from backend.extractors.social_extractor import extract_social_links

url = "https://bharatplastic.org/"

social = extract_social_links(url)

print()
print("=" * 60)

if not social:
    print("No social media links found.")
else:
    print(f"Found {len(social)} social media links:\n")

    for item in social:
        print(item)

print("=" * 60)
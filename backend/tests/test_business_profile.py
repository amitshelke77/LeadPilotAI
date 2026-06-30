from pprint import pprint

from backend.extractors.business_profile import extract_business_profile

url = "https://bharatplastic.org/"

profile = extract_business_profile(url)

print()
pprint(profile)
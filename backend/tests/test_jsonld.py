import json
import requests
from bs4 import BeautifulSoup

url = "https://bharatplastic.org/"

response = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=15,
)

soup = BeautifulSoup(response.text, "html.parser")

scripts = soup.find_all("script", type="application/ld+json")

print(f"\nFound {len(scripts)} JSON-LD blocks\n")

for i, script in enumerate(scripts, start=1):

    print("=" * 60)
    print(f"BLOCK {i}")
    print("=" * 60)

    if script.string:
        print(script.string[:1000])

    print()
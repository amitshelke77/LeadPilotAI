import re
import requests
from bs4 import BeautifulSoup

EMAIL_REGEX = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

url = "https://bharatplastic.org"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers, timeout=15)

print("\nStatus:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

pages = [url]

print("\nContact Links Found:")

for link in soup.find_all("a", href=True):

    href = link["href"]

    if "contact" in href.lower():

        print(href)

        if href.startswith("http"):
            pages.append(href)
        else:
            pages.append(url.rstrip("/") + "/" + href.lstrip("/"))

print("\nPages to Scan:")

for page in pages:

    print(page)

print("\nEmails Found:")

for page in pages:

    try:

        r = requests.get(page, headers=headers, timeout=15)

        emails = re.findall(EMAIL_REGEX, r.text)

        print(f"\n{page}")

        print(emails)

    except Exception as e:

        print(e)
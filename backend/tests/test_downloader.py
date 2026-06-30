from backend.extractors.email.utils.downloader import download_html

url = "https://bharatplastic.org"

html = download_html(url)

print()

print("=" * 60)
print("Downloaded HTML")
print("=" * 60)

print(f"Length : {len(html)} characters")

print()

print(html[:1000])
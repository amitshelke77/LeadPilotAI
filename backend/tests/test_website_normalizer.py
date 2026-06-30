from backend.normalizers.website_normalizer import normalize_website


urls = [

    "https://www.bharatplastic.org",

    "http://bharatplastic.org/",

    "bharatplastic.org",

    "https://bharatplastic.org/contact",

    "https://bharatplastic.org/about",

]

print()

for url in urls:

    print(url)

print()

print("Normalized")

for url in urls:

    print(normalize_website(url))
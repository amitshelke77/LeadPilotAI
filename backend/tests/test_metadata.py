from backend.extractors.metadata_extractor import extract_metadata

url = "https://bharatplastic.org/"

data = extract_metadata(url)

print()

for key, value in data.items():

    print(f"{key:15} : {value}")
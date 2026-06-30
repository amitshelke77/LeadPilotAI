from backend.enrichers.extraction_engine import run_extractors

url = "https://bharatplastic.org"

evidence = run_extractors(url)

print()

print("=" * 60)

print(f"Collected {len(evidence)} evidence objects")

print("=" * 60)

for item in evidence:
    print(item)
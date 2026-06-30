from backend.extractors.registry import EXTRACTORS

print()

print("=" * 60)

print(f"Registered Extractors: {len(EXTRACTORS)}")

print()

for extractor in EXTRACTORS:
    print(extractor["name"])

print()

print("=" * 60)
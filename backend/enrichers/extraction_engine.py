from backend.extractors.registry import EXTRACTORS
from backend.enrichers.evidence import Evidence


def run_extractors(url: str) -> list[Evidence]:
    """
    Runs every registered extractor.

    Returns a flat list of Evidence objects.
    """

    all_evidence = []

    for extractor in EXTRACTORS:

        print(f"\nRunning {extractor['name']} extractor...")

        try:

            result = extractor["function"](url)

            if result is None:
                continue

            if isinstance(result, list):
                all_evidence.extend(result)
            else:
                all_evidence.append(result)

        except Exception as e:

            print(f"{extractor['name']} extractor failed")
            print(e)

    return all_evidence
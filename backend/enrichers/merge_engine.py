from collections import defaultdict

from backend.enrichers.evidence import Evidence


def merge_evidence(evidence_list: list[Evidence]):

    merged = {}

    grouped = defaultdict(list)

    for item in evidence_list:
        grouped[item.field].append(item)

    for field, values in grouped.items():

        best = max(values, key=lambda x: x.confidence)

        merged[field] = {
            "value": best.value,
            "confidence": best.confidence,
            "source": best.source,
            "sources": [v.source for v in values],
            "evidence_count": len(values),
        }

    return merged
from backend.enrichers.evidence import Evidence


evidence = Evidence(
    field="phone",
    value="+91-9860256222",
    source="jsonld",
    confidence=1.0,
)

print()
print(evidence)
print()
print(evidence.field)
print(evidence.value)
print(evidence.source)
print(evidence.confidence)
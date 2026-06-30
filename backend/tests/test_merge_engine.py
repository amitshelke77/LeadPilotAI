from pprint import pprint

from backend.enrichers.evidence import Evidence
from backend.enrichers.merge_engine import merge_evidence


evidence = [

    Evidence(
        field="phone",
        value="9860256222",
        source="footer",
        confidence=0.75,
    ),

    Evidence(
        field="phone",
        value="+91-9860256222",
        source="jsonld",
        confidence=1.00,
    ),

    Evidence(
        field="phone",
        value="9860256222",
        source="contact",
        confidence=0.90,
    ),

    Evidence(
        field="company",
        value="Bharat Plastic Manufacturing Co.",
        source="jsonld",
        confidence=1.00,
    ),

    Evidence(
        field="company",
        value="Bharat Plastic",
        source="metadata",
        confidence=0.80,
    ),

]

profile = merge_evidence(evidence)

print()

pprint(profile)
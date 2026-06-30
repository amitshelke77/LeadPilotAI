from pprint import pprint

from backend.enrichers.evidence import Evidence
from backend.enrichers.profile_builder import build_business_profile

evidence = [

    Evidence(
        field="company",
        value="Bharat Plastic Manufacturing Co.",
        source="jsonld",
    ),

    Evidence(
        field="website",
        value="https://bharatplastic.org",
        source="jsonld",
    ),

    Evidence(
        field="phone",
        value="+91-9860256222",
        source="jsonld",
    ),

    Evidence(
        field="description",
        value="Plastic manufacturing company",
        source="metadata",
    ),

    Evidence(
        field="linkedin",
        value="https://linkedin.com/company/demo",
        source="html",
    ),

]

profile = build_business_profile(evidence)

print()
pprint(profile)
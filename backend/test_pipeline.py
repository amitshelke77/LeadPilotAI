from backend.pipeline.lead_pipeline import generate_leads

leads = generate_leads(
    "Plastic Manufacturers",
    "Pune",
    5,
)

for lead in leads:
    print("=" * 50)
    print(lead)
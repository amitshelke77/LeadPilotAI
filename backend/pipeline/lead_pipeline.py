import pandas as pd

from backend.models.company import Company


class LeadPipeline:

    def __init__(self):
        self.companies = []

    def add(self, company: Company):
        self.companies.append(company)

    def to_dataframe(self):

        rows = []

        for company in self.companies:
            rows.append(
                {
                    "Company": company.company,
                    "Location": company.location,
                    "Website": company.website,
                    "Email": company.email,
                    "Phone": company.phone,
                    "Source": company.source,
                }
            )

        df = pd.DataFrame(rows)

        if not df.empty:
            df = df.drop_duplicates(subset=["Company", "Website"])

        return df
from backend.normalizers.email_normalizer import normalize_email_list


emails = [
    "Sales@BharatPlastic.Org",
    " sales@bharatplastic.org ",
    "INFO@Company.COM",
    "info@company.com",
    "invalid@email",
    "hello",
    "",
]

print()

print("Original")

for email in emails:
    print(email)

print()

print("Normalized")

for email in normalize_email_list(emails):
    print(email)
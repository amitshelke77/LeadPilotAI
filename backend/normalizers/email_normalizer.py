import re


EMAIL_REGEX = re.compile(
    r"^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[A-Za-z]{2,}$"
)


def normalize_email(email: str) -> str | None:

    if not email:
        return None

    email = email.strip().lower()

    if not EMAIL_REGEX.match(email):
        return None

    return email


def normalize_email_list(email_list):

    normalized = set()

    for email in email_list:

        clean = normalize_email(email)

        if clean:
            normalized.add(clean)

    return sorted(normalized)
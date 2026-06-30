import re


def normalize_phone(phone: str) -> str | None:
    """
    Normalize Indian phone numbers.

    Examples

    +91 9860256222  -> 9860256222
    +91-9860256222  -> 9860256222
    919860256222    -> 9860256222
    09860256222     -> 9860256222
    """

    if not phone:
        return None

    # Keep only digits
    phone = re.sub(r"\D", "", phone)

    # Remove country code
    if phone.startswith("91") and len(phone) == 12:
        phone = phone[2:]

    # Remove leading zero
    if phone.startswith("0") and len(phone) == 11:
        phone = phone[1:]

    # Final validation
    if len(phone) != 10:
        return None

    if phone[0] not in "6789":
        return None

    return phone


def normalize_phone_list(phone_list):

    normalized = set()

    for phone in phone_list:

        clean = normalize_phone(phone)

        if clean:
            normalized.add(clean)

    return sorted(normalized)
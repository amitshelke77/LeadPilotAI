from dataclasses import dataclass


@dataclass
class Company:
    company: str
    location: str
    website: str = ""
    email: str = ""
    phone: str = ""
    source: str = ""
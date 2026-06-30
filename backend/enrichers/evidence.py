from dataclasses import dataclass


@dataclass
class Evidence:
    field: str
    value: str
    source: str
    confidence: float = 1.0
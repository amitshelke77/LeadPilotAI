from backend.normalizers.phone_normalizer import normalize_phone_list


phones = [
    "+91 9860256222",
    "+91-9860256222",
    "919860256222",
    "9860256222",
    "09860256222",
    "3199002617",
]


print()

print("Original")

for phone in phones:
    print(phone)

print()

print("Normalized")

for phone in normalize_phone_list(phones):
    print(phone)
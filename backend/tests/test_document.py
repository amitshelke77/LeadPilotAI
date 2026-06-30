from backend.web.document import Document


url = "https://bharatplastic.org"

document = Document.from_url(url)

print()

print("=" * 60)
print("Document")
print("=" * 60)

print()

print("URL")
print(document.url)

print()

print("TITLE")
print(document.title)

print()

print("HTML LENGTH")
print(len(document.html))

print()

print("TEXT LENGTH")
print(len(document.text))

print()

print("META TAGS")
print(len(document.meta))

print()

print("LINKS")
print(len(document.links))

print()

print("SCRIPTS")
print(len(document.scripts))
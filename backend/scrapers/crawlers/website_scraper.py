from bs4 import BeautifulSoup
import requests


def find_contact_page(url: str):

    try:

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=15,
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser",
        )

        keywords = [
            "contact",
            "contact-us",
            "about",
            "reach-us",
        ]

        for link in soup.find_all("a", href=True):

            href = link["href"].lower()

            for keyword in keywords:

                if keyword in href:

                    if href.startswith("http"):
                        return href

                    return url.rstrip("/") + "/" + href.lstrip("/")

    except Exception:
        return None

    return None
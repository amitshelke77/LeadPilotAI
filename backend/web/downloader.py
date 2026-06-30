import requests


DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/138.0 Safari/537.36"
    )
}


def download_html(url: str) -> str:
    """
    Downloads the HTML of a webpage.

    Raises:
        requests.HTTPError if download fails.
    """

    response = requests.get(
        url,
        headers=DEFAULT_HEADERS,
        timeout=20,
    )

    response.raise_for_status()

    return response.text
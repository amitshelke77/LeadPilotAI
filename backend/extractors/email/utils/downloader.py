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
    Downloads HTML from a webpage.

    Returns:
        HTML string

    Raises:
        requests.HTTPError
    """

    response = requests.get(
        url,
        headers=DEFAULT_HEADERS,
        timeout=20,
    )

    response.raise_for_status()

    return response.text
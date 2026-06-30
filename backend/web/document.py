from dataclasses import dataclass

from bs4 import BeautifulSoup

from backend.web.downloader import download_html
from backend.web.parser import parse_html


@dataclass
class Document:

    url: str
    html: str
    soup: BeautifulSoup

    @classmethod
    def from_url(cls, url: str):

        html = download_html(url)

        soup = parse_html(html)

        return cls(
            url=url,
            html=html,
            soup=soup,
        )

    @property
    def title(self):

        if self.soup.title:

            return self.soup.title.get_text(strip=True)

        return ""

    @property
    def text(self):

        return self.soup.get_text(" ", strip=True)

    @property
    def links(self):

        links = []

        for a in self.soup.find_all("a", href=True):

            links.append(a["href"])

        return links

    @property
    def scripts(self):

        return self.soup.find_all("script")

    @property
    def meta(self):

        meta = {}

        for tag in self.soup.find_all("meta"):

            name = tag.get("name") or tag.get("property")

            content = tag.get("content")

            if name and content:

                meta[name.lower()] = content

        return meta
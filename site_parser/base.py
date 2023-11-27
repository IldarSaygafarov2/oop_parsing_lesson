import requests
from bs4 import BeautifulSoup
import config


class BaseParser:
    host: str = config.HOST

    @staticmethod
    def get_soup(url: str = host) -> BeautifulSoup:
        """Get html code of the page by url."""
        response = requests.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")



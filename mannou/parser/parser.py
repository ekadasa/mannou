# -*- coding: utf-8 -*-

"""Main module for parsing sites

This module contains class that used for parsing sites.

"""


from abc import ABC, abstractmethod
from typing import NamedTuple

from bs4 import BeautifulSoup

from .. import util
from ..exception import URLError

__all__ = ['Image', 'Chapter', 'MangaPage']


class Image(NamedTuple):
    """Represent an image.

    Args:
        name (str): The Image name with extension.
        url (str): The source of image.

    """
    name: str
    url: str


class Chapter(NamedTuple):
    """Represent a chapter.

    Args:
        number (str): The chapter number.
            str is used over int due there is some 'decimal' chapter, like 10.5.
            Why do not use float? It is weird to see chapter 1.0, I think.
        url (str): The url of specific chapter.

    """
    number: str
    url: str

class Manga(ABC):
    """An abstract base class for manga site parser.

    Every parser class must inherit this class to ensure that every
    parser has the same functionality. The subclass is also must has
    `domain` attribute to check whether `url` argument is valid url
    or not.

    Attributes:
        domain (str): Domain of the site

    Args:
        url (str): Url of the manga.
        soup (BeautifulSoup): `BeautifulSoup` object from url.

    """

    def __init__(self, url):
        valid_url = self.check_url(url)

        if not valid_url:
            raise URLError(f"Url must started with http(s)://{self.domain}")

        self.url = url
        self.soup = util.make_soup(url)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.url}')"

    @classmethod
    def check_url(cls, url):
        return False if url.find(cls.domain) == -1 else True

    def __str__(self):
        return self.title

    def __iter__(self):
        for chapter in self.chapters:
            yield chapter

    def __reversed__(self):
        for chapter in reversed(self.chapters):
            yield chapter

    def __len__(self):
        return len(self.chapters)

    def __init_subclass__(cls, domain, **kwargs):
        cls.domain = domain
        super().__init_subclass__(**kwargs)

    @property
    @abstractmethod
    def title(self):
        """str: Get the title of manga

        """
        pass

    @property
    @abstractmethod
    def chapters(self):
        """list(Chapter): Get chapter number and url in manga

        """
        pass


    @abstractmethod
    def get_chapter_images(self, chapter_url):
        """list(Image): Get image name and url in chapter

        You can override this method as static method.
        """
        pass

    def filter_chapters(self, start=0, stop=None):
        """Filter chapter in manga.

        This is general algorithm for class parser that follow the rules.
        You may or may not override this method.

        Args:
            start (int, float): From what chapter?
            stop (int, float, optional): What chapter to stop? default to None.

        """
        last_chapter = float(self.chapters[-1].number)
        end_chapter = stop if stop is not None else last_chapter

        filtered = []
        for chapter in self.chapters:
            chapter_number = float(chapter.number)
            if chapter_number >= float(start) and chapter_number <= end_chapter:
                filtered.append(chapter)

        return filtered

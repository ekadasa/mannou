# -*- coding: utf-8 -*-

"""Parser module for manga website.

This module is used for parsing manga website.

"""


from abc import ABC, abstractmethod
from typing import NamedTuple

from bs4 import BeautifulSoup

from . import exception, util


__all__ = ['Image', 'Chapter', 'Manga']


class Image(NamedTuple):
    """Represent an image.

    Parameters
    ----------
    name : str
        The image name with extension.
    url : str
        The image source.

    """
    name: str
    url: str


class Chapter(NamedTuple):
    """Represent a chapter.

    Parameters
    ----------
    number : str
        The chapter number.
        str is used over int due there is some 'decimal' chapter, like 10.5.
        Why do not use float? It is weird to see chapter 1.0, I think.
    url : str
        The url of specific chapter.

    """
    number: str
    url: str

class Manga(ABC):
    """An abstract base class for manga site parser.

    Every parser class must inherit this class to ensure that every
    parser has the same functionality. The subclass also must has
    `domain` attribute to check whether `url` argument is valid url
    or not.

    Attributes
    ----------
    domain : str
        Domain of the site

    Parameters
    ----------
    url : str
        Url of the manga.
    soup : :obj:`BeautifulSoup`
        `BeautifulSoup` object from url.

    Raises
    ------
    URLError
        If not `url` is not a valid url.

    """

    def __init__(self, url):
        valid_url = self.check_url(url)

        if not valid_url:
            message = f"Url must started with http(s)://{self.domain}"
            raise exception.URLError(message)

        self.url = url
        self.soup = util.make_soup(url)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.url}')"

    def __str__(self):
        return self.title

    def __getitem__(self, key):
        return self.chapters[key]

    def __setitem__(self, key, value):
        self.chapters[key] = value

    def __delitem__(self, key):
        del self.chapters[key]

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
        """str: The title of manga

        """
        pass

    @property
    @abstractmethod
    def chapters(self):
        """:obj:`list` of :obj:`mannou.parser.Chapter`: Available chapters.

        """
        pass


    @abstractmethod
    def get_chapter_images(self, chapter_url):
        """Parse `chapter_url`.

        Returns
        -------
        :obj:`list` of :obj: `mannou.parser.Image`
            List of images name and source location.

        You can override this method as static method.
        """
        pass

    @classmethod
    def check_url(cls, url):
        """Check whether `url` is actually from `self.domain` or not.

        Parameters
        ----------
        url : str
            URL that you want to check.

        Returns
        -------
        bool
            True if it is url from `self.domain`, False otherwise.

        """
        return False if url.find(cls.domain) == -1 else True

    def filter_chapters(self, start=0, stop=None):
        """Filter chapter in manga.

        This is general algorithm for class parser that follow the rules.
        You may or may not override this method.

        Parameters
        ----------
        start : int, float, optional
            From what chapter? Default to 0.
        stop : int, float, optional
            What chapter to stop? default to None.

        Returns
        -------
        :obj:`list` of :obj:`mannou.parser.Chapter`
            Filtered chapters.

        """
        last_chapter = float(self.chapters[-1].number)
        end_chapter = stop if stop is not None else last_chapter

        filtered = []
        for chapter in self.chapters:
            chapter_number = float(chapter.number)
            if chapter_number >= float(start) and chapter_number <= end_chapter:
                filtered.append(chapter)

        return filtered

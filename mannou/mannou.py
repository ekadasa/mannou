# -*- coding: utf-8 -*-

"""Main module for downloading manga.

See Also
--------
`mannou.api` : An implementation for this module.

"""


from pathlib import Path

from . import exception, util
from .site.komikid import Komikid
from .site.manganelo import Manganelo


__all__ = ['Mannou']


class Mannou:
    """Main class for `mannou`.

    This class used for unify the parsers and downloading manga.

    Attributes
    ----------
    parsers : :obj:`list` of :class: subclassing :class:`mannou.parser.Manga`
        The stable parsers class that can parser certain site.
    parser : :class: subclassing :class:`mannou.parser.Manga`
        The used parser.
    manga : :obj: of :class: subclassing :class:`mannou.parser.Manga`
        An object that have an ability to parse `url`.
    root : :obj:`pathlib.Path`
        The save location in your machine.

    Parameters
    ----------
    url : str
        Manga's url.
    parser : :class:, optional
        Custom class for parsing `url`. It recommended if this class
        subclassing `mannou.parser.Manga`

    Raises
    ------
    URLError
        If `url` is not an url.

    """
    parsers = [Manganelo, Komikid]
    parser = None
    manga = None
    root = Path.home().joinpath('Manga')

    def __init__(self, url, parser=None):
        self.url = url

        if not util.is_url(url):
            raise exception.URLError(url, 'is not an url.')

        if parser is None:
            self.set_parser()
        else:
            self.parser = parser

    def set_parser(self):
        """Set `self.parser` to correct parser.

        """
        for parser in self.parsers:
            if parser.check_url(self.url):
                self.parser = parser

    def parse(self):
        """Assign `self.manga` to :obj:`self.parser`

        Raises
        ------
        ParserNotFoundError
            If `self.parser` is None

        """
        if self.parser is None:
            message = ("self.parser is None, you can specify parser "
                       "by your self or use set_parser().")
            raise exception.ParserNotFoundError(message)

        self.manga = self.parser(self.url)

    def download(self, start=0, end=None):
        """Download manga and save it in local machine.

        Parameters
        ----------
        start : int, float, optional
            The first chapter, default to 0.
        end : int, float, optional
            The last chapter that you want to download, default to None.

        Returns
        -------
        :obj:`pathlib.Path`
            Saved manga directory if succeeded.

        """
        util.mkdir(self.root)

        if self.parser is None:
            self.set_parser()

        if self.manga is None:
            self.parse()

        manga_dir = self.root.joinpath(self.manga.title)
        util.mkdir(manga_dir)

        chapters = self.manga.filter_chapters(start, end)
        for number, url in chapters:
            util.clear_screen()
            print("Title          :", self.manga.title)
            print("Chapter        :", number)
            print("Latest Chapter :", self.manga.chapters[-1].number)
            print("Save Location  :", manga_dir)
            print()

            chap_dir = manga_dir.joinpath(number)
            util.mkdir(chap_dir)

            images = self.manga.get_chapter_images(url)
            for name, source in images:
                image_path = chap_dir.joinpath(name)
                print("Downloading", name)
                util.download(source, image_path)

        return manga_dir

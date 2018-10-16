# -*- coding: utf-8 -*-

from pathlib import Path

from . import util, exception
from .site.komikid import Komikid
from .site.manganelo import Manganelo


class Mannou:
    parsers = [Manganelo, Komikid]
    parser = None
    manga = None
    root = Path.home().joinpath('Manga')

    def __init__(self, url, parser=None):
        self.url = url
        if parser is None:
            self.set_parser()
        else:
            self.parser = parser


    def set_parser(self):
        for parser in self.parsers:
            if parser.check_url(self.url):
                self.parser = parser

    def parse(self):
        if self.parser is None:
            message = ("self.parser is None, you can specify parser "
                       "by your self or use set_parser().")
            raise exception.ParserNotFoundError(message)

        self.manga = self.parser(self.url)

    def download(self, start=0, end=None):
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
                util.download(str(source), image_path)

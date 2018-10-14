# -*- coding: utf-8 -*-

import pathlib

from . import anilist, mannou, util


def info(search):
    """Get an anime info.

    It can search by url or title of the manga.

    Parameters
    ----------
    search : str
        Anime title or url that you want to search.

        Please remember searching by url takes longer than by name because
        it needs to parse an url first to get manga's title


    Returns
    -------
    dict
        Manga information.

    """
    manga_name = search
    an_url = util.is_url(search)

    if an_url:
        manga = get(search)
        manga_name = manga.title

    info = anilist.MangaInfo(manga_name)
    return info.info()

def get(url, parser=None):
    manga = mannou.Mannou(url)

    if parser is not None:
        manga.parser = parser

    manga.parse()
    return manga.manga

def download(url, parser=None, save_location=None, **limits):

    manga = mannou.Mannou(url)

    if save_location is not None:
        manga.root = pathlib.Path(save_location)

    if parser is not None:
        manga.parser = parser

    start = limits['start'] if 'start' in limits else 0
    end = limits['end'] if 'end' in limits else None

    manga.parse()
    manga.download(start=start, end=end)

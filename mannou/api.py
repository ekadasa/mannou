# -*- coding: utf-8 -*-

"""Main `Mannou` API.

This module provide the easy way to use `mannou.anilist.AniList`
and `mannou.mannou.Mannou`.

Note
----
Every functions in this module are imported in main package `mannou`.
If you want to use `mannou.api.get` function, you only need to type `mannou.get`.

    Please use `mannou.AniList` and `mannou.Mannou`

See Also
--------
`mannou.AniList` : main class for getting manga info.
`mannou.Mannou` : main class for downloading manga.

"""


import pathlib

from . import anilist, mannou, util


__all__ = ['info', 'get', 'download']

def info(search):
    """Get an anime info.

    It can search by url or title of the manga.

    Parameters
    ----------
    search : str
        Anime title or url that you want to search.

        Please remember searching by url takes longer than by name because
        it needs to parse an url first to get manga's title.

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

    info = anilist.AniList(manga_name)
    return info.info()

def get(url, parser=None):
    """Get manga chapters.

    Returns
    -------
    :obj: `mannou.parser.Manga` subclass.
        It will return correct :obj: that handle `url` specified in
        `mannou.Mannou.parsers`.

    :obj: `parser`
        If `parser` is not None

    """
    manga = mannou.Mannou(url)

    if parser is not None:
        manga.parser = parser

    manga.parse()
    return manga.manga

def download(url, parser=None, save_location=None, **limits):
    """Download chapter(s) in specified `url`.

    It will download chapter(s) in and save it in your machine.

    Parameters
    ----------
    url : str
        URL of manga that you want to download.
    parser : `class`, optional
        Custom parser to parse `url`.
        It preferred that `parser` is subclassing `mannou.parser.Manga`.
    save_location : str, optional
        The save location, the default is ``~/home`` for UNIX
        or ``%USERPROFILE%\\Manga`` for Windows.
    start : int, float, optional.
        The starting chapter, default to 0.
    end : int, float, optional.
        The last chapter that you want to download, default to None.

    Returns
    -------
    :obj: of `pathlib.Path`
        The saved location in your machine.

    """

    manga = mannou.Mannou(url)

    if save_location is not None:
        manga.root = pathlib.Path(save_location)

    if parser is not None:
        manga.parser = parser

    start = limits['start'] if 'start' in limits else 0
    end = limits['end'] if 'end' in limits else None

    manga.parse()
    return manga.download(start=start, end=end)

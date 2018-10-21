# -*- coding: utf-8 -*-

"""Main `Mannou` API.

A **command line interface** for `mannou`. This command::

    $ mannou

is as same as::

    $ python3 -m mannou

Example
-------
For downloading manga from *'https://manganelo.com/manga/aiura'*,
from chapter 2 to 3, you can type::

    $ mannou https://manganelo.com/manga/aiura --start 2 --end 3


For further feature, please type::

    $ mannou --help

"""


import argparse
import pathlib
import sys

import urllib3

from . import anilist, exception, mannou


__all__ = ['main', 'cli']

def main():
    """Main function.

    This function will run if you type::

        $ mannou

    in your terminal.

    """
    try:
        cli()
    except KeyboardInterrupt:
        print('Program interrupted by User.')
        sys.exit()

def cli():
    """Main cli function.

    """
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    parser = argparse.ArgumentParser()
    parser.add_argument('url', type=str, help="URL of the manga")
    parser.add_argument('--download', '-d', action='store_true', help='Download manga.')
    parser.add_argument('--start', '-s', type=float, default=0)
    parser.add_argument('--end', '-e', type=float)
    parser.add_argument('--dest', type=str, help="Download location")

    args = parser.parse_args()
    manga = mannou.Mannou(args.url)

    try:
        manga.parse()
    except exception.ParserNotFoundError:
        print('Sorry, we do not support', manga.url)
        sys.exit()

    if args.download:
        if args.dest is not None:
            manga.root = pathlib.Path(args.dest)

        manga.download(start=args.start, end=args.end)

    else:
        info = anilist.AniList(manga.manga.title).info()
        description = info['description'].replace('<br>', '')
        detailed_info = f"""
        ID
        --
          > Anilist        : {info['id']}
          > MyAnimeList    : {info['idMal']}

        Title
        -----
          > Romaji         : {info['title']['romaji']}
          > English        : {info['title']['english']}
          > Native         : {info['title']['native']}
          > User Preffered : {info['title']['userPreferred']}

        Genre(s)
        --------
          > {', '.join(info['genres'])}

        Description
        -----------
          > {description}

        Last Available Chapters
        -----------------------
          > Chapter {manga.manga.chapters[-1].number}
            `- {manga.manga.chapters[-1].url}

        More Info
        ---------
          > {info['siteUrl']}
          > https://myanimelist.net/manga/{info['idMal']}
        """

        for line in detailed_info.splitlines():
            indent = 8
            if line[:indent] == ' ' * indent:
                print(line[indent:])
            else:
                print(line)

        # chapters = manga.manga.filter_chapters(args.start, args.end)
        # for chapter in chapters:
        #     print('  > Chapter', chapter.number)
        #     print('    `-', chapter.url)

# -*- coding: utf-8 -*-

"""Main Test for ``mannou.api``

"""

import shutil
import tempfile

import mannou
from mannou.site.komikid import Komikid
from mannou.site.manganelo import Manganelo


MANGA_NAMES = ('Komi-san wa Komyushou Desu', 'Tomo-chan wa Onnanoko!')
MANGA_URLS = ('https://manganelo.com/manga/komisan_wa_komyushou_desu',
              'http://www.komikid.com/manga/angel-beats-heavens-door')

def test_info():
    # By Name
    for title in MANGA_NAMES:
        info = mannou.info(title)
        assert isinstance(info['id'], int)

    # By URL
    for url in MANGA_URLS:
        parser = Manganelo if url.find('manganelo') != -1 else None
        info = mannou.info(url, parser=parser)
        assert isinstance(info['id'], int)

def test_get():
    for url in MANGA_URLS:
        parser = Komikid if url.find('komikid') != -1 else None
        manga = mannou.get(url, parser=parser)
        images = manga.get_chapter_images(manga[0].url)
        assert images[0].name == '1.jpg'

def test_download():
    # Because every chapter is almost short chapter
    url = 'https://manganelo.com/manga/tomochan_wa_onnanoko'
    dest = tempfile.mkdtemp()

    try:
        manga_loc = mannou.download(url, parser=Manganelo,
                                    save_location=dest, start=14, end=14)

        assert str(manga_loc.parent) == dest
    except AssertionError as err:
        print(err)
        raise AssertionError
    else:
        shutil.rmtree(dest)

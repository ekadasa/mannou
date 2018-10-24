# -*- coding: utf-8 -*-
"""Main test for ``mannou.mannou.Mannou``.

"""

import pathlib
import shutil
import tempfile

import mannou
from mannou.site.manganelo import Manganelo


def test_mannou():
    url = 'https://manganelo.com/manga/tomochan_wa_onnanoko'
    dest = tempfile.mkdtemp()
    manga = mannou.Mannou(url)
    manga.parser = Manganelo
    manga.root = pathlib.Path(dest)
    try:
        manga_loc = manga.download(start=14, end=14)
        assert str(manga_loc.parent) == dest
    except AssertionError as err:
        print(err)
        raise AssertionError
    finally:
        shutil.rmtree(dest)

# -*- coding: utf-8 -*-

"""Test module for `mannou.util`

"""

import pathlib

import pytest

from mannou import util

def test_mkdir():
    test_dir = pathlib.Path.home().joinpath('mannou_test')

    if test_dir.exists():
        created = util.mkdir(test_dir)
        assert not created
    else:
        created = util.mkdir(test_dir)
        util.rmdir()
        assert created

def test_is_url():
    urls = ['http://manganelo.com',
            'https://www.manganelo.com']

    for url in urls:
        valid_url = util.is_url(url)
        assert valid_url

    not_urls = ['manganelo.com', 'mangatown']
    for not_url in not_urls:
        valid_url = util.is_url(not_url)
        assert not valid_url

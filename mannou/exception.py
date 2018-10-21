# -*- coding: utf-8 -*-

"""Main exception module.

Every exception must be listed in here.

"""

from urllib.error import HTTPError, URLError


class ParserNotFoundError(Exception):
    """Raise when url there is no parser found in `mannou.Mannou.parsers`.

    """

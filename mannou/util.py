# -*- coding: utf-8 -*-

"""Utility modules.

This module contains miscellaneous function used in every other packages and
or modules.

Notes
-----
If module grow complex, there is a chance to group similar function
in the new modules.

"""

import math
import os
import pathlib
import urllib

import bs4
import requests
import tqdm

from . import exception


__all__ = [
    'mkdir',
    'clear_screen',
    'is_url',
    'get_200',
    'make_soup',
    'download',
    'StatusCode'
]

def mkdir(dirpath):
    """Create a directory.

    Only create directory if ``dirpath`` is not exists.
    ``dirpath`` must be an object from ``pathlib.Path``

    Parameters
    ----------
    dirpath : :obj:`pathlib.Path`

    Returns
    -------
    bool
        True if successful, False otherwise.

    """
    if not dirpath.exists():
        dirpath.mkdir()
        return True
    else:
        return False

def clear_screen():
    """Clear terminal screen.

    Only work for Windows and UNIX-like OS.

    """
    os.system('cls' if os.name == 'nt' else 'clear')

def is_url(url):
    """Validate url.

    Parameters
    ----------
    url : str
        An url to validate.

    Returns
    -------
    bool
        True if valid url, False otherwise.

    """
    try:
        result = urllib.parse.urlparse(url)
        return all([result.scheme, result.netloc])
    except AttributeError:
        return False

def get_200(url, max_retries=10, **options):
    """Sends GET request until it get 200.

    By default, it will try 10 times before raise.

    Parameters
    ---------
    url : str
        URL that you want to GET
    max_retries : int, optional
        Decide how many times sending GET request before raise.
    user_agent : str, optional
        User agent that you want to use
    stream : bool, optional
        Decide if you want to stream or not.

    Returns
    -------
    :obj:`requests.Response`

    Raises
    ------
    HTTPError
        If `max_retries` exceeded.

    """
    mozilla_ua = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    user_agent = options['user_agent'] if 'user_agent' in options else mozilla_ua
    stream = options['stream'] if 'stream' in options else False

    headers = {'User-Agent': user_agent}

    for _ in range(max_retries):
        try:
            response = requests.get(url, headers=headers, verify=False)
            response.raise_for_status()
        except exception.HTTPError as error:
            # Sometimes certain website return server error
            # (Such as bad gateway), sometimes it can be fixed with make request
            # twice or thrice
            if error.code >= StatusCode.INTERNAL_SERVER_ERROR:
                continue
            else:
                raise HTTPError(error.url, error.code, error.msg, error.hdrs, error.fp)
        else:
            return response

def make_soup(url):
    """Create `bs4.BeautifulSoup` object from url.

    Parameters
    ----------
    url : str
        URL that you want to scrap.

    Returns
    -------
    :obj:`bs4.BeautifulSoup`

    Raises
    ------
    exception.HTTPError
        From `mannou.util.get_200`

    """
    response = get_200(url)
    return bs4.BeautifulSoup(response.text, 'html.parser')

def download(url, filepath):
    """Downloader, with progress bar.

    Send GET request and save it to local computer.

    Parameters
    ----------
    url : str
        URL that you want to download.
    filepath : :obj:`str`
        Saved file location

    """
    response = get_200(url, stream=True)

    # Total size in bytes.
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024
    wrote = 0
    with open(filepath, 'wb') as f:
        for data in tqdm.tqdm(response.iter_content(block_size),
                              total=math.ceil(total_size//block_size),
                              unit='KB',
                              unit_scale=True):
            wrote = wrote + len(data)
            f.write(data)


class StatusCode:
    """A bunch of HTTP status codes.

    Every HTTP status code stored in readable attributes name.

    """
    OK = 200
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500

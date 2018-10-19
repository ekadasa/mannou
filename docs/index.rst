Mannou: Manga Downloader
########################

|pypi| |version| |travis| |docs|

**Mannou** is a manga downloader for various sites.
It can be used as *library* or *command line application*.

.. note:: Please remember this project still under development and created by a new programmer.

-----------------------------------------------------------------------------------------------


Mannou In Action
----------------

Download your favorite manga via *command line*:

.. code-block:: bash

    $ mannou https://manganelo.com/manga/aiura --download --start 2 --end 3

This command will download a manga called **Aiura** from chapter 2 to 3
and save it in ``~/Manga/Aiura``.


You can also use **Mannou** as library:

.. code-block:: python

    >>> import mannou
    >>> manga = mannou.get('https://manganelo.com/manga/aiura')
    >>> manga.title
    Aiura
    >>> manga.chapter[0]
    Chapter(number='1', url='https://manganelo.com/chapter/aiura/chapter_1')
    >>> images = manga.get_chapter_images(manga.chapter[0].url)
    >>> images[0]
    Image(name='1.jpg', url='http://s8.mkklcdn.com/mangakakalot/a1/aiura/chapter_1/1.jpg')


Features
--------

* Get manga info in-depth (using Anilist_ API)
* Download some or all chapters in certain manga.


The User Guide
--------------

This part of the documentation, which is mostly prose, begins with some
background information about Requests, then focuses on step-by-step
instructions for getting the most out of Requests.

.. toctree::
   :maxdepth: 2

   user/intro
   user/install
   user/quickstart
   user/cli
   user/advanced


-----------------------------------------------------------------------------------------------

The end.

.. _AniList: https://anilist.co/

.. |travis| image:: https://img.shields.io/travis/borderlineargs/mannou.svg
    :target: https://travis-ci.org/borderlineargs/mannou
    :alt: Build status of the master branch on linux (Ubuntu Xenial).

.. |pypi| image:: https://img.shields.io/pypi/v/mannou.svg
    :target: https://pypi.org/project/mannou/
    :alt: PyPI.

.. |version| image:: https://img.shields.io/pypi/pyversions/mannou.svg
    :target: https://pypi.org/project/mannou/
    :alt: Python supported version.

.. |docs| image:: https://readthedocs.org/projects/mannou/badge/
    :target: https://mannou.readthedocs.io/
    :alt: Documentation.

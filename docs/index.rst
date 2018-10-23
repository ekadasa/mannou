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
    >>> url = 'https://manganelo.com/manga/aiura'
    >>> manga = mannou.get(url)
    >>> str(manga) # or manga.title
    Aiura
    >>> manga[0] # or manga.chapters[0]
    Chapter(number='1', url='https://manganelo.com/chapter/aiura/chapter_1')
    >>> images = manga.get_chapter_images(manga[0].url)
    >>> images[0]
    Image(name='1.jpg', url='http://s8.mkklcdn.com/mangakakalot/a1/aiura/chapter_1/1.jpg')
    >>> mannou.download(url, start=1, end=5) # Download every chapters 1 until 5 in 'Aiura' and save it to default location (~/Manga or %USERPROFILE%\Manga)


Features
--------

* Get manga info in-depth (using Anilist_ API)
* Download some or all chapters in certain manga


Website Support
---------------

* `Manganelo <https://manganelo.com>`_ (English Language)
* `Komikid <http://komikid.com>`_ (Bahasa Indonesia)


The User Guide
--------------

This guide explain how you can use **Mannou**.

.. toctree::
   :maxdepth: 2

   user/intro
   user/install
   user/quickstart
   user/cli
   user/advanced


Source Documentation
--------------------

This section provides source documentation.

.. toctree::
    :maxdepth: 2

    api/mannou
    api/mannou.site
    api/modules

-----------------------------------------------------------------------------------------------

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

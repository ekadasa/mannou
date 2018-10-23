.. _quickstart:


Quickstart
==========

This page provide the fastest way to getting started

First, make sure Mannou is :ref:`installed <installation>`.

Let's get started with some simple examples.


Getting Manga Information
-------------------------

Begin by importing the Mannou module::

    >>> import mannou

Let's try get manga information. You can pass manga name::

    >>> info = mannou.info('Aiura')

or manga url::

    >>> info = mannou.info('https://manganelo.com/manga/aiura')

Now, our info is an object from :class:`dict`, containing manga information.
It is just a regular :obj:`dict`::

    >>> info.keys()
    dict_keys(['id', 'idMal', 'title', ... , 'siteUrl'])
    >>> info['id']
    75890
    >>> info['genres']
    ['Comedy', 'Slice of Life']

.. note:: Passing an url instead manga's name is actually
    slower because Mannou need to parse first to get manga's name.


Parsing Manga Site
------------------

This module is useful when you want to parse a web page.

As usual, you import `mannou` first, then::

    >>> manga = mannou.get('https://manganelo.com/manga/aiura')


``manga`` is a :obj:`Manga <mannou.parser.Manga>` object.
This object can be used to parse every images in
every chapters in Aiura::

    >>> str(manga) # or manga.title
    'Aiura'
    >>> manga[0] # or manga.chapters[0]
    Chapter(number='1', url='https://manganelo.com/chapter/aiura/chapter_1')

A ``manga.chapters[0]`` is a :obj:`list`
of :obj:`Chapter <mannou.parser.Chapter>`.
It is just an object of :obj:`namedtuple`.
Use this information to parse images.::

    >>> images = manga.get_chapter_images(manga[0].url)

``get_chapter_images`` is a method for getting all images in certain chapter.
In this example we want to get all images in chapter 1 of Aiura.

    >>> images[0] # first page
    Image(name='1.jpg', url='http://s8.mkklcdn.com/mangakakalot/a1/aiura/chapter_1/1.jpg')
    >>> images[-1] # last page
    Image(name='14.jpg', url='http://s8.mkklcdn.com/mangakakalot/a1/aiura/chapter_1/14.jpg')

:class:`Image <mannou.parser.Image>` is an :obj:`namedtuple`,
just like :class:`Chapter <mannou.parser.Chapter>`.


Downloading Manga
-----------------

If you want to download manga, the easiest way is::

    >>> url = 'https://manganelo.com/manga/aiura'
    >>> mannou.download(url)
    PosixPath('/home/<username>/Manga/Aiura')

This line will download every chapters in Aiura and save it in default
location (``~/Manga`` in Linux or ``%USERPROFILE%\Manga`` in Windows).
It will return save location in
:obj:`PosixPath` or :obj:`WindowsPath` in your machine.


If you want to download only chapter 3 to 4, use parameter ``**limits``::

    >>> mannou.download(url, start=3, end=4)

Maybe you want to save the manga in different location,
use parameter ``save_location``.::

    >>> mannou.download(url, save_location='/home/<username>/Comic/')
    PosixPath('/home/<username>/Comic/')

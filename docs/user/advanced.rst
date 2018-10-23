.. _advanced:


Advanced Usage
==============

This page provide advanced usage you can do in this package.


Create Custom Site Parser
-------------------------

Do you have your favorite manga website and preferring to
download manga from there, but not supported in this package?
Just create your own! What you must do are:

* Make it inherit :class:`Manga <mannou.parser.Manga>`
* Override all ``abstractmethod`` and have return
  value as same as ``super().__doc__``.
* Override method ``filter_chapters`` if it doesn't work in
  your custom parser.


Use Custom Site Parser
----------------------

Just pass your custom parser in parameter ``parser``
if you use main API (``info``, ``get``, and ``download``), or
if you use :class:`Mannou <mannou.mannou.Mannou>`, please
see `Mannou`_ section.::

    >>> from your_module import YourParser
    >>> url = 'https://manganelo.com/manga/aiura'
    >>> info = mannou.download(url, parser=YourParser)


AniList
-------

:class:`Anilist <mannou.anilist.AniList>` is the main class
for communicating with AniList API, basic usage::

    >>> from mannou import anilist
    >>> a = anilist.AniList('Aiura')

Now, ``a`` is an :obj:`Anilist <mannou.anilist.Anilist>` object.
You can use method ``json`` to return JSON from AniList API.::

    >>> a.json()
    {
      'data': {
        'Media': {
          'id': 75980,
          ...
          'siteUrl': 'https://anilist.co/manga/75980
        }
      }
    }

Or you can use method ``info`` to return parsed data as :obj: `dict`.::

    >>> a.info()
    {
      'id': ['75980'],
      ...
      'siteUrl': 'https://anilist.co/manga/75980
    }

If you are not satisfied with the default result,
you can modify attribute ``query`` as you wish.
But in order to do so, you must familiar with Anilist API
and how GraphQL works.::

    >>> a.query = """
    ... query ($name: String) {
    ...   Media (search: $name, type: MANGA) {
    ...     ...
    ...   }
    ... }
    ... """ # Your long long query
    >>> a.json() # The result will be follow your query.

For further detail, please read this::
* `AniList API Documentation <https://anilist.gitbook.io/anilist-apiv2-docs/>`_
* `GraphQL <http://graphql.org>`_


Mannou
------

:class:`Mannou <mannou.mannou.Mannou>` is the main class
for downloading manga. Basic usage::

    >>> from mannou.mannou import Mannou
    >>> url = 'https://manganelo.com/manga/aiura'
    >>> m = Mannou(url)

If you have your custom parser, you can pass it
in parameter ``parser`` directly::

    >>> m = Mannou(url, parser=YourParser)

It will change value of attribute ``parser``
to your custom parser. You can set it like this too::

    >>> m.parser = YourParser

You can also append your custom parser in attribute ``parsers``.
``parsers`` is containing list of available parser in this package.::

    >>> m.parsers.append(YourParser)

then set it automatically by calling ``set_parser`` method::

    >>> m.set_parser()

By default, every manga will be saved it ``~/Manga`` or
``%USERPROFILE%\Manga``. You can override it by modify ``root`` attribute.
Please remember root attribute must be :class:`Path <pathlib.Path>` object.::

    >>> import pathlib
    >>> m.root = pathlib.Path.home().joinpath('Comic') # ~/Comic or %USERPROFILE%\\Comic

If preparation have already completed, download your manga by::

    >>> m.download()

It will download every chapter in *https://manganelo.com/manga/aiura*.
You can limit it by using parameter ``start`` and ``end``::

    >>> m.download(3, 7)

or be explicit::

    >>> m.download(start=3, end=7)

It will download only chapter 3 to chapter 7.

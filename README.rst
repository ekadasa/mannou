Mannou - Manga Downloader
#########################

|pypi| |pyver| |travis|

A manga downloader from various sites.

Please remember this package still under development.

This command:

.. code-block:: bash

    $ mannou https://manganelo.com/manga/tomochan_wa_onnanoko --download

will download every chapters to ``~/Manga``

.. contents::


Features
========

* Get info and download every chapters from supported sites.


Installation
============

You must have Python_ and PIP installed in your computer, then:

.. code-block:: bash

    $ pip install mannou

.. _Python: https://www.python.org/


Examples
========

You can use this package as CLI program or import it in your project.


CLI
---

.. code-block:: bash

    $ mannou https://manganelo.com/manga/aiura --download --start 2 --end 3

This command will download manga called *Aiura* from chapter 2 to 3

Project
-------

.. code-block:: python

    >>> import mannou
    >>> manga = mannou.get('https://manganelo.com/manga/aiura')
    >>> manga.title
    Aiura
    >>> manga.chapter[0]
    Chapter(number='1', url='https://manganelo.com/chapter/aiura/chapter_1')


Documentation
=============

Please refer to https://mannou.readthedocs.io for further documentation.


License
=======
Free software: `GNU General Public License v3`_.

.. _`GNU General Public License v3`: https://github.com/borderlineargs/mannou/blob/master/LICENSE


Credits
=======

* This package use AniList_ api to get manga's info.
* This package structure is heavily influenced by cookiecutter-pypackage_
  and the requests_.

.. _AniList: https://anilist.co/
.. _cookiecutter-pypackage: https://github.com/audreyr/cookiecutter-pypackage
.. _requests: https://github.com/requests/requests


.. |travis| image:: https://img.shields.io/travis/borderlineargs/mannou.svg
    :target: https://travis-ci.org/borderlineargs/mannou
    :alt: Build status of the master branch on linux (Ubuntu Xenial)

.. |pypi| image:: https://img.shields.io/pypi/v/mannou.svg
    :target: https://pypi.org/project/mannou/
    :alt: PyPI

.. |pyver| image:: https://img.shields.io/pypi/pyversions/mannou.svg
    :target: https://pypi.org/project/mannou/
    :alt: Python supported version.

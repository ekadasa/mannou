.. _cli:

Command Line Interface
======================

You can use Mannou as standalone program. The most basic example
to use this is:

.. code-block:: bash

    $ mannou https://manganelo.com/manga/aiura

This command will print an info about manga called *Aiura*.
Id you want to download, use ``--download`` or ``-d`` flag.

.. code-block:: bash

    $ mannou https://manganelo.com/manga/aiura --download

It will download every chapter available in Aiura and save it
to your machine (default is ``~/Manga/<MangaName>`` or
``%USERPROFILE%\Manga\MangaName``). You can change save location
by using ``--dest`` flag.

.. code-block:: bash

    $ mannou  https://manganelo.com/manga/aiura -d --dest /home/<username>/Comic/

To limit what chapters to download, use ``--start`` or ``-s``
and ``--end`` or ``-e`` respectively. The command below will download
chapter 3 until chapter 4.

.. code-block:: bash

    $ mannou  https://manganelo.com/manga/aiura -d --start 3 --end 4

.. note:: You **don't** need to remember any of those command. Just use flag
    ``--help`` or ``-h`` and you are good to go.

    .. code-block:: bash

        $ mannou --help

.. _installation:


Installation of Mannou
======================

This part of the documentation covers the installation of **Mannou**.
If you are an experienced Python developer, then just skip
into `Installing Mannou`_ section.


Installing Python
-----------------

But of course, you must have python installed in your machine.
Verify first by typing:

.. code-block:: bash

    $ python3 --version

if you use UNIX-like environment (Linux or MacOS), or:

.. code-block:: batch

    > python --version

if you use Windows.


If the command is not recognized or the version is below 3.6, visit
`Python <https://www.python.org/>`_ and follow the install instructions.


Installing PIP
--------------

Usually PIP already included in Python Windows installer, but not in Linux.
Verify first before installing PIP by typing:

.. code-block:: bash

    $ pip3 --version

for Linux, or:

.. code-block:: batch

    > pip --version

for Windows.


If there is no PIP installed, please install it first by:

.. code-block:: bash

    $ apt-get update
    $ apt-get install python-pip3

On Debian-based Linux. You may need administrative privilege to install.

.. note:: For MacOS or other Linux distribution,
    please follow official guide for each vendor.


Installing Virtual Environment (Optional)
-----------------------------------------

It is recommended to use virtual environment to separate each projects.
You can use ``venv``, ``virtualenv``, ``pipenv``,
or any virtual environment you prefer.

* `Venv website <https://docs.python.org/3/library/venv.html>`_
* `Virtualenv website <https://virtualenv.pypa.io>`_
* `Pipenv website <https://pipenv.readthedocs.io>`_


Installing Mannou
-----------------

To install Mannou, run this in your terminal:

.. code-block:: bash

    $ pip install mannou

And done!

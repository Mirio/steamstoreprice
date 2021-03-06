Getting Start
=============

Link
----
    * GitHub: `   https://github.com/Mirio/steamstoreprice/tree/master <https://github.com/Mirio/steamstoreprice/tree/master>`_
    * Documentation: `http://steamstoreprice.readthedocs.org/ <http://steamstoreprice.readthedocs.org/>`_
    * PYPI: `https://pypi.python.org/pypi/steamstoreprice <https://pypi.python.org/pypi/steamstoreprice>`_


Badge
-----

.. image:: https://travis-ci.org/Mirio/steamstoreprice.svg?branch=0.1
    :target: https://travis-ci.org/Mirio/steamstoreprice

.. image:: https://img.shields.io/pypi/dm/steamstoreprice.svg
    :target: https://pypi.python.org/pypi/steamstoreprice

.. image:: https://img.shields.io/github/downloads/mirio/steamstoreprice/total.svg
    :target: https://github.com/Mirio/steamstoreprice/tree/0.1

.. image:: https://readthedocs.org/projects/steamstoreprice/badge/?version=0.1
    :target: http://steamstoreprice.readthedocs.org/en/latest/?badge=0.1
    :alt: Documentation Status

Features
--------
    * Easy to find the price without using the Amazon API
    * Easy to use
    * Python 3.x +
    * Unittest
    * Custom Errors


Installation via Pip
--------------------

.. code-block:: bash
    :name: installation

    pip install steamstoreprice


Installation from Source
------------------------

.. code-block:: bash
    :name: installation_source

    git clone https://github.com/Mirio/steamstoreprice.git
    cd steamstoreprice
    python setup.py install


Uninstall via Pip
-----------------

.. code-block:: bash
    :name: installation

    pip uninstall steamstoreprice


Basic usage
-----------

Code:

.. code-block:: python
    :name: code

    from steamstoreprice import SteamStorePrice

    url = "http://store.steampowered.com/app/349040/"
    pricelib = SteamStorePrice()
    print(pricelib.getprice(url))


Output:

.. code-block:: bash
    :name: code

    $ python example_getprice.py
    49.99


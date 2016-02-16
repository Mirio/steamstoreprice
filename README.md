## SteamStorePrice
This module find the price from url given

[![Build Status](https://travis-ci.org/Mirio/steamstoreprice.svg?branch=0.1)](https://travis-ci.org/Mirio/steamstoreprice) [![PyPI](https://img.shields.io/pypi/dm/steamstoreprice.svg)]() [![Github All Releases](https://img.shields.io/github/downloads/mirio/steamstoreprice/total.svg)]() [![Documentation Status](https://readthedocs.org/projects/steamstoreprice/badge/?version=0.1)](http://steamstoreprice.readthedocs.org/en/latest/?badge=0.1)
[![Coverage Status](https://coveralls.io/repos/github/Mirio/steamstoreprice/badge.svg?branch=0.1)](https://coveralls.io/github/Mirio/steamstoreprice?branch=0.1)



## Link
Documentation: http://steamstoreprice.readthedocs.org/

Bug Tracker: https://github.com/Mirio/steamstoreprice/issues

GitHub: https://github.com/Mirio/steamstoreprice


## Requirement
Python 3.x

Python Library = [ 'requests', 'beautifulsoup4' ]

## How to install
```
pip install steamstoreprice
```

## Install from source
```
git clone https://github.com/Mirio/steamstoreprice.git
cd steamstoreprice
python setup.py install
```

## Getting Started

Example:
```
from steamstoreprice import SteamStorePrice

url = "http://store.steampowered.com/app/349040/"
pricelib = SteamStorePrice()
print(pricelib.getprice(url))
```

Output:
```
$ python example_getprice.py
49.99
```

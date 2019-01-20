# pydsb

Unofficial DSBmobile API written in Python.

![](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)
[![PyPI](https://img.shields.io/pypi/v/pydsb.svg?style=flat-square&colorB=dfb317)](https://pypi.org/project/pydsb/)

## Installation

```bash
pip3 install pydsb
```

## Usage

```python
import pydsb

dsb = pydsb.PyDSB("username", "password")
dsb.login()

timetables = dsb.get_timetables()
news = dsb.get_news()
```

## Made with

- [Requests](https://github.com/requests/requests/) - HTTP requests

## Meta

Lucas Hild - [https://lucas-hild.de](https://lucas-hild.de)  
This project is licensed under the MIT License - see the LICENSE file for details

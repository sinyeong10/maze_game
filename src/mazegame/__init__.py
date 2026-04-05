#!/usr/bin/env python
# coding=utf-8
import logging
from ._compat import NullHandler

#@todo log level 적용하기
logging.getLogger(__name__).addHandler(NullHandler())

__author__ = 'V.hs sin'
__email__ = 'cbrnt1210@gmail.com'
__version__ = '1.0.0'
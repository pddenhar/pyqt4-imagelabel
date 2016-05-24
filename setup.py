#!/usr/bin/env python

from distutils.core import setup

setup(
  name = "qt4ImageLabel",
  version = "0.1",
  description = "Subclass of QLabel that takes a pixmap and draws it H+V centered and at the correct aspect ratio.",
  py_modules = ["qt4ImageLabel"],
  author='Peter Den Hartog',
  author_email='pddenhar@gmail.com',
  url='https://github.com/pddenhar/pyqt4-imagelabel')
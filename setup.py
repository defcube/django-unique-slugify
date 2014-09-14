#!/usr/bin/env python
from distutils.core import setup


readme = open('README.rst').read()

setup(
    name='django-unique-slugify',
    version='1.01',
    author_email='gattster@gmail.com',
    author='SmileyChris (packaged by Philip Gatt)',
    description="Automatically create a unique slug for a model.",
    long_description=readme,
    url='http://github.com/defcube/django-unique-slugify',
    py_modules=['django_unique_slugify'],
    data_files=[('', ['README.rst'])],
    )
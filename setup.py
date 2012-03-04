#!/usr/bin/env python
from setuptools import setup
name = 'opendata'
setup(
    name             = name,
    author           = 'Andrei Fokau',
    url              = 'https://github.com/andreif/opendata',
    version          = __import__(name).__version__,
    packages         = [name],
    include_package_data = True,
    package_data     = {name: ['data/*.*']},
)

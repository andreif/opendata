#!/usr/bin/env python
from setuptools import setup
name = 'opendata'
setup(
    name             = name,
    author           = 'Andrei Fokau',
    author_email     = 'andrei@5monkeys.se',
    url              = 'https://github.com/andreif/opendata',
    download_url     = 'https://nodeload.github.com/andreif/opendata/tarball/master',
    version          = __import__(name).__version__,
    packages         = [name],
    include_package_data = True,
    package_data     = {name: ['data/*.*']},
)

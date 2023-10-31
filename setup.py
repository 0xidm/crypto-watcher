# -*- coding: utf-8 -*-
# idm

from setuptools import setup, find_packages
import os
import re


def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)


def read(fname):
    return open(fpath(fname)).read()


file_text = read(fpath('crypto_watcher/__meta__.py'))


def grep(attrname):
    pattern = r"{0}\W*=\W*'([^']+)'".format(attrname)
    strval, = re.findall(pattern, file_text)
    return strval


setup(
    version=grep('__version__'),
    name='crypto_watcher',
    description="Crypto Price Watcher",
    packages=find_packages(),
    scripts=[
        "scripts/crypto-watcher",
    ],
    # long_description=read('../Readme.md'),
    include_package_data=True,
    keywords='',
    author=grep('__author__'),
    author_email=grep('__email__'),
    url=grep('__url__'),
    install_requires=[
        "web3==5.31.4",
        "SQLAlchemy==1.4.42",
        "click==8.1.3",
        "python-dotenv",
        "pycoingecko",
        "psycopg2-binary",
        "requests",
        "alembic",
        "multicall",
    ],
    license='MIT',
    zip_safe=False,
)

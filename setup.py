#!/usr/bin/env python

from setuptools import setup

setup(
    name='Foodcheck',
    version='1.0',
    description='OpenShift Python 2.6 Django',
    author='Tim Austen, Eileen Lin, Richard Esplin',
    author_email='richard-oss@esplins.org',
    url='http://www.python.org/sigs/distutils-sig/',
    install_requires=['Django==1.3',
                      'psycopg2',
                      # 'pymongo',
    ],
 )

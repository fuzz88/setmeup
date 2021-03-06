#!/usr/bin/env python3
from setuptools import setup

version = open('VERSION').read().strip()

setup(
    name='setmeup',
    version=version,
    description='Runtime settings for minimalists',
    url='https://github.com/szastupov/setmeup',
    license='MIT',
    author='Stepan Zastupov',
    author_email='stepan.zastupov@gmail.com',

    py_modules=['setmeup'],

    keywords='environ settings env config',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries'
    ]
)

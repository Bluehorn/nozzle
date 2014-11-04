# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='nozzle',
    version='0.0.1',

    description='Another inversion of control container for Python',
    url='https://github.com/Bluehorn/nozzle',

    author='Torsten Landschoff',
    author_email='torsten@landschoff.net',

    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='dependency injection ioc container',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    # dev and test requirements, install via
    # $ pip install -e .[dev,test]
    extras_require = {
        'dev': ['check-manifest'],
        'test': ['pytest'],
    },

    # No entry points yet. We may have a tool that checks if all classes with injection
    # decoration can be built.
    entry_points={},
)

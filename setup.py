#!/usr/bin/env python3

from setuptools import setup, find_packages

exec(open('pytus2000/__init__.py').read())

setup(
    name='pytus2000',
    version=__version__,
    description='A library for working with the UK Time Use Study 2000 data.',
    maintainer='Tim Tröndle',
    maintainer_email='tt397@cam.ac.uk',
    url='https://www.github.com/timtroendle/pytus2000',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    install_requires=[],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering'
    ]
)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', 'PyYAML==3.12', ]

setup_requirements = ['pytest-runner', 'pytest-cov', ]

test_requirements = ['pytest', ]

setup(
    author="Luke Smith",
    author_email='lsmith@zenoscave.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Smoke and I/o testing with any language through unittests",
    entry_points={
        'console_scripts': [
            'smokr=smokr.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='smokr',
    name='smokr',
    packages=find_packages(include=['smokr']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/Lsmith-Zenoscave/smokr',
    version='0.2.0',
    zip_safe=False,
)

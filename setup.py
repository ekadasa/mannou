# -*- coding: utf-8 -*-

"""The setup script."""

import pathlib

from setuptools import find_packages, setup


here = pathlib.Path(__file__).parent

with open(here.joinpath('README.rst')) as readme_file:
    readme = readme_file.read()

with open(here.joinpath('HISTORY.rst')) as history_file:
    history = history_file.read()

requirements = ['requests>=2.19.0', 'beautifulsoup4>=4.6.0', 'tqdm>=4.26.0']

setup_requirements = ['pytest-runner']

test_requirements = ['pytest']

setup(
    author="Muhammad Adi Prasojo",
    author_email='borderlineargs@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="A manga downloader from various sites.",
    entry_points={
        'console_scripts': [
            'mannou=mannou.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='mannou',
    name='mannou',
    packages=find_packages(include=['mannou', 'mannou.site']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/borderlineargs/mannou',
    version='0.1.0',
    zip_safe=False,
)

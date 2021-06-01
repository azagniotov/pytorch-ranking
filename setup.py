#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""Setup dot py."""
from __future__ import absolute_import, print_function

# import re
from glob import glob
from os.path import basename, dirname, join, splitext

from setuptools import find_packages, setup


def read(*names, **kwargs):
    """Read description files."""
    path = join(dirname(__file__), *names)
    with open(path, encoding=kwargs.get('encoding', 'utf8')) as fh:
        return fh.read()

long_description = '{}\n{}'.format(
    read('README.rst'),
    read(join('docs', 'CHANGELOG.rst')),
    )

setup(
    name='PyTorch Ranking',
    version='0.0.1',
    description='PyTorch Ranking is a library for Learning-to-Rank (LTR) techniques on the PyTorch platform.',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    license='MIT License',
    author='Alexander Zagniotov',
    author_email='azagniotov@gmail.com',
    url='https://github.com/azagniotov/pytorch-ranking',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(i))[0] for i in glob("src/*.py")],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list:
        # http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Programming Language :: Python :: 3.8',
        'Topic :: Information Retrieval :: Learning-to-Rank',
        ],
    project_urls={
        'webpage': 'https://github.com/azagniotov/pytorch-ranking',
        'Documentation': 'https://pytorch-ranking.readthedocs.io/en/latest/',
        'Changelog': 'https://github.com/azagniotov/pytorch-ranking/blob/master/docs/CHANGELOG.rst',
        'Issue Tracker': 'https://github.com/azagniotov/pytorch-ranking/issues',
        },
    keywords=[
        'ltr', 'pytorch-ranking', 'listwise', 'pairwise', 'pointwise', 'information retrieval',
        'machine-learning', 'information-retrieval', 'deep-learning', 'ranking', 'learning-to-rank',
        'recommender-systems',
        ],
    python_requires='>=3.8, <3.9',
    install_requires=[
        'matplotlib>=3',
        # eg: 'aspectlib==1.1.1', 'six>=1.7',
        ],
    extras_require={
        # eg:
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
        },
    setup_requires=[
        #   'pytest-runner',
        #   'setuptools_scm>=3.3.1',
        ],
    entry_points={
        'console_scripts': [
            'pytorch_ranking_cli= entry_point:main',
            ]
        },
    )

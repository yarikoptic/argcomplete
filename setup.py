#!/usr/bin/env python

import glob

from setuptools import find_packages, setup

install_requires = []
lint_require = ["flake8", "mypy"]
tests_require = ["coverage", "pexpect", "wheel"] + lint_require
importlib_backport_requires = ["importlib-metadata >= 0.23, < 6"]

setup(
    name="argcomplete",
    version="2.0.4",
    url="https://github.com/kislyuk/argcomplete",
    project_urls={
        "Documentation": "https://kislyuk.github.io/argcomplete",
        "Source Code": "https://github.com/kislyuk/argcomplete",
        "Issue Tracker": "https://github.com/kislyuk/argcomplete/issues",
        "Change Log": "https://github.com/kislyuk/argcomplete/blob/master/Changes.rst",
    },
    license="Apache Software License",
    author="Andrey Kislyuk",
    author_email="kislyuk@gmail.com",
    description="Bash tab completion for argparse",
    long_description=open("README.rst").read(),
    python_requires=">=3.6",
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        "test": tests_require,
        "lint": lint_require,
        ':python_version == "3.6"': importlib_backport_requires,
        ':python_version == "3.7"': importlib_backport_requires,
    },
    packages=find_packages(exclude=["test"]),
    scripts=glob.glob("scripts/*"),
    package_data={"argcomplete": ["bash_completion.d/python-argcomplete"]},
    zip_safe=False,
    include_package_data=True,
    platforms=["MacOS X", "Posix"],
    test_suite="test",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Shells",
        "Topic :: Terminals",
    ],
)

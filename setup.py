#! /usr/bin/env python3

from setuptools import setup

with open("README.md") as fi:
    long_description=fi.read()

setup(

    name="f1-2019-telemetry",
    version="1.1.3",

    author="Sidney Cadot",
    author_email="sidney@jigsaw.nl",

    description="A package to handle UDP telemetry data as sent by the F1 2019 game.",
    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://gitlab.com/reddish/f1-2019-telemetry/",

    # Since we don't have __init__.py files, our packages aren't found by setuptools.find_packages().
    # We therefore specify them explicitly here.
    packages=['f1_2019_telemetry', 'f1_2019_telemetry.tools'],

    entry_points={
        'console_scripts': [
            'f1-2019-telemetry-recorder=f1_2019_telemetry.tools.recorder:main',
            'f1-2019-telemetry-player=f1_2019_telemetry.tools.player:main',
            'f1-2019-telemetry-monitor=f1_2019_telemetry.tools.monitor:main'
        ]
    },

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Games/Entertainment",
        "Operating System :: OS Independent"
    ],

    python_requires=">=3.6"
)

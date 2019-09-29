#! /usr/bin/env python3

from setuptools import setup, find_packages

long_description=\
"""This package provides functionality to handle UDP telemetry data as sent by the F1 2019 game.

The F1 2019 game can send UDP packets containing live data for an ongoing race.
The format of these packets is documented by CodeMasters.
This package provides ctype-based definitions of all packet types that the game sends.

In addition to that, the package also provides command line tools to record, playback,
and monitor game session data. These tools are useful by themselves, but also serve as
examples of how to capture and decode live game data in Python.
"""

setup(

    name="f1-2019-telemetry",
    version="1.0.1",

    author="Sidney Cadot",
    author_email="sidney@jigsaw.nl",

    description="A package to handle UDP telemetry data as sent by the F1 2019 game.",
    long_description=long_description,
    long_description_content_type="text/plain",

    url="https://github.com/sidneycadot/f1-2019-telemetry/",

    packages=find_packages(),

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

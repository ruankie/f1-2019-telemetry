#! /usr/bin/env python3

from setuptools import setup, find_packages

long_description=\
"""This package provides functionality to handle UDP telemetry data from the F1 2019 game.

The F1 2019 game can optionally send UDP packets containing data for an ongoing race. The format
of these packets is documented by CodeMasters. This package provides ctype-based definitions of
all packet types that the program may send.

Apart from that, this package also provides some command line tools to record and playback
race sessions, and to show data on a currently running race session.
"""

setup(

    name="f1-2019-telemetry",
    version="1.0.1",

    author="Sidney Cadot",
    author_email="sidney@jigsaw.nl",

    description="A package to handle UDP telemetry data from the F1 2019 game.",
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

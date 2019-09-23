#! /usr/bin/env python3

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="f1_2019_telemetry",
    version="1.0",
    author="Sidney Cadot",
    author_email="sidney@jigsaw.nl",
    description="A package to handle UDP telemetry data from the F1 2019 game.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sidneycadot/f1-2019-telemetry/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Games/Entertainment",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6"
)


F1 2019 UDP Telemetry support package
=====================================

The f1-2019-telemetry package implements support for interpreting telemetry information as sent out over the network by the F1 2019 game.
It also implements several small tools to record, playback, and monitor F1 2019 session data.

The core functionality is based on the CodeMasters Forum topic documenting the F1 2019 packet format: https://forums.codemasters.com/topic/38920-f1-2019-udp-specification/

The package should work on Python 3.6 and above.


Project information
-------------------

The f1-2019-telemetry package and its documentation are currently at version **1.0.1**.

The project is distributed as a standard wheel package on PyPI.
This allows installation using the standard Python _pip_ tool as follows:

    pip install f1-2019-telemetry

The project is hosted on Github: http://www.github.com/sidneycadot/f1-2019-telemetry/

The PyPI page for the package is here: https://pypi.org/project/f1-2019-telemetry/1.0.1/

The package documentation can be read here: http://f1-telemetry-2019.readthedocs.io/


Description of toplevel project files and directories
-----------------------------------------------------

| name               | description                                                                                              |
| ------------------ | -------------------------------------------------------------------------------------------------------- |
| README.md          | README file for the Git project                                                                          |
| LICENSE            | Project license (MIT)                                                                                    |
| RELEASE-HOWTO.txt  | Step-by-step instructions for creating a release. tion                                                   |
| setup.py           | Setup file for creating distributions                                                                    |
| dump_tables.py     | Python script to create ReST and Markdown style tables from data used in the specification               |
| docs/              | Documentation of the project (based on Sphinx)                                                           |
| f1_2019_telemetry/ | The main package of the project                                                                          |
| make-dist.sh       | Maintainer script to build a wheel distribution file using a local Python 3 instance (setuptools, wheel) |
| upload-dist.sh     | Maintainer script to upload the package to PyPI using a local Python 3 instance (twine)                  |
| local-install.sh   | Maintainer script to install the wheel distribution file to a local Python 3 instance (pip)              |
| make-docs.sh       | Maintainer script to build the documentation using a local Python 3 instance (sphinx)                    |
| run-recorder.sh    | Maintainer script to run the f1-2019-telemetry-recorder script from a local Python 3 instance            |

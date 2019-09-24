#! /bin/sh

set -e

export PATH=$HOME/local_python/root/bin:$PATH

# Clean up
rm -rf build dist f1_2019_telemetry.egg-info *.whl

python3 setup.py bdist_wheel

cp dist/*.whl .

# Clean up
rm -rf build dist f1_2019_telemetry.egg-info

unzip -v *.whl

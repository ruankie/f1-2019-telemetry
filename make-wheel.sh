#! /bin/sh

set -e

if [ -z $LOCAL_PYTHON3_BIN ] ; then
    echo "Please define LOCAL_PYTHON3_BIN environment variable."
    exit 1
fi

export PATH=$LOCAL_PYTHON3_BIN:$PATH

# Clean up
rm -rf build dist f1_2019_telemetry.egg-info *.whl

python3 setup.py bdist_wheel

cp dist/*.whl .

# Clean up everything except wheel file
rm -rf build dist f1_2019_telemetry.egg-info

# Show contents of wheel file
unzip -v *.whl

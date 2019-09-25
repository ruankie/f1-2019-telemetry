#! /bin/sh

set -e

if [ -z $LOCAL_PYTHON3_BIN ] ; then
    echo "Please define LOCAL_PYTHON3_BIN environment variable."
    exit 1
fi

export PATH=$LOCAL_PYTHON3_BIN:$PATH

# Start afresh
rm -rf source/generated build

sphinx-apidoc -o source/generated ../f1_2019_telemetry

make html

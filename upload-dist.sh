#! /bin/sh

set -e

if [ -z $LOCAL_PYTHON3_BIN ] ; then
    echo "Please define LOCAL_PYTHON3_BIN environment variable."
    exit 1
fi

export PATH=$LOCAL_PYTHON3_BIN:$PATH

python3 -m twine upload dist/*

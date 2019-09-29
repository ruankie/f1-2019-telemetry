#! /bin/sh

set -e

if [ -n $LOCAL_PYTHON3_BIN ] ; then
    export PATH=$LOCAL_PYTHON3_BIN:$PATH
fi

python3 -m twine upload dist/*

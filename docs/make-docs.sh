#! /bin/sh

set -e

export PATH=$HOME/local_python/root/bin:$PATH

# Start afresh
rm -rf build

make html

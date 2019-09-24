#! /bin/sh

set -e

export PATH=$HOME/local_python/root/bin:$PATH

pip3 uninstall -y f1-2019-telemetry

pip3 install *.whl

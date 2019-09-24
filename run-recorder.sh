#! /bin/sh

set -e

export PATH=$HOME/local_python/root/bin:$PATH

python3 -m f1_2019_telemetry.recorder

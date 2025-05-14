#!/bin/bash
. /opt/conda/etc/profile.d/conda.sh && conda activate geodiffgrid
exec "$@"

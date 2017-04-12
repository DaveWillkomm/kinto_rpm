#!/usr/bin/env bash
set -evx

vagrant ssh -c '${HOME}/kinto_rpm/bin/build/buildrpm.sh'

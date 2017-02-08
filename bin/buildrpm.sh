#!/usr/bin/env bash
set -evx

vagrant ssh -c 'sudo ${HOME}/kinto_rpm/bin/build/buildrpm.sh'

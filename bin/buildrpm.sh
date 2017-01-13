#!/usr/bin/env bash
set -evx
vagrant ssh -c "/opt/kinto_rpm/bin/build/buildrpm.sh"

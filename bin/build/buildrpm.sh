#!/usr/bin/env bash
set -evx

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
rpmbuild -bb --define="_topdir ${project_dir}" "${project_dir}/SPECS/kinto.spec"

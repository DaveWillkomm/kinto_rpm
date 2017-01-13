#!/usr/bin/env bash
set -evx

kinto_rpm_dir="/opt/kinto_rpm"
rpmbuild -bb --define="_topdir ${kinto_rpm_dir}" "${kinto_rpm_dir}/SPECS/kinto.spec"

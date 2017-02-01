#!/usr/bin/env bash
set -evx

curl -L https://centos7.iuscommunity.org/ius-release.rpm > /tmp/ius-release.rpm
set +e
yum -y install /tmp/ius-release.rpm
set -e
yum -y install \
  postgresql-devel \
  python35u-devel \
  python35u-pip \
  python35u-setuptools \
  rpmdevtools \
  rpmlint \
  tmux \
  tree

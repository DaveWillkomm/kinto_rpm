#!/usr/bin/env bash
set -evx

curl -L https://centos7.iuscommunity.org/ius-release.rpm > /tmp/ius-release.rpm
set +e
yum -y install /tmp/ius-release.rpm
set -e
yum -y install \
  postgresql-devel \
  python36u-devel \
  python36u-pip \
  python36u-setuptools \
  rpmdevtools \
  rpmlint \
  tmux \
  tree

mkdir -p /opt/kinto
chown vagrant:vagrant /opt/kinto

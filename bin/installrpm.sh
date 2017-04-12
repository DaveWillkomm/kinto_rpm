#!/usr/bin/env bash
if [[ ! ${1} ]]; then
  echo "Kinto version required, e.g. 6.0.3"
  exit 0
fi

set -evx
vagrant up test
vagrant scp RPMS/**/kinto-${1}-*.rpm test:~/
vagrant ssh test -c "sudo yum -y install kinto-${1}-*.rpm"

# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure('2') do |config|
  config.vm.box = 'centos/7'

  # I was unable to successfully change the default synced folder's provider to vboxsf for bi-directional syncing, so I
  # disabled it and configured a separate folder.
  config.vm.synced_folder '.', '/vagrant', disabled: true
  config.vm.synced_folder '.', '/opt/kinto_rpm', provider: :vboxsf

  config.vm.define 'build', primary: true do |build|
    build.vm.provision 'shell', path: 'bin/build/provision.sh'
  end

  config.vm.define 'test', autostart: false do |test|
    test.vm.provision 'shell', path: 'bin/test/provision.sh'
  end
end

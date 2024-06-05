# Vagrant Cloud Images

Purpose of this project is to provide [Vagrant Box images](https://app.vagrantup.com/cloud-image) based on public
colud images of various GNU/Linux distributions with no modifications at
all (or, at least, the minimum possible).

| distribution | version | vagrant box | method |
| ------------ | :-----: | ----------- | ------ |
| AlmaLinux | 9.4 | almalinux-9.4 | cloud-init injection |
| AlmaLinux | 8.10 | almalinux-8.10 | cloud-init injection |
| Debian | 12 | debian-12 | cloud-init injection |
| Debian | 11 | debian-11 | cloud-init injection |
| Debian | 10 | debian-10 | cloud-init injection |
| Fedora | 40 | fedora-40 | cloud-init injection |
| Fedora | 39 | fedora-39 | cloud-init injection |
| Ubuntu | 24.04 | ubuntu-24.04 | cloud-init injection |
| Ubuntu | 22.04 | ubuntu-22.04 | cloud-init injection |
| Ubuntu | 20.04 | ubuntu-20.04 | cloud-init injection |
| Ubuntu | 18.04 | ubuntu-18.04 | cloud-init injection |
| Ubuntu | 16.04 | ubuntu-16.04 | cloud-init injection |
| Ubuntu | 14.04 | ubuntu-14.04 | cloud-init injection |

## cloud-init injection

This method consists to inject a `cloud-init` configuration file under
`/etc/cloud/cloud.cfg.d/99_vagrant.cfg` with a content similar to the
following:

```yaml
datasource_list: [ NoCloud, None ]
ssh_pwauth: True
users:
  - name: vagrant
    plain_text_passwd: vagrant
    sudo: ALL=(ALL) NOPASSWD:ALL
    shell: /bin/bash
    lock_passwd: false
    ssh_authorized_keys:
      # https://github.com/hashicorp/vagrant/tree/master/keys
      - 'ssh-rsa ... vagrant insecure public key'
```

That ensure the creation of Vagrant user during the first boot by the
`cloud-init` service included in every GNU/Linux cloud images.

Packer is not used at all. The disk image are downloaded, mounted, injected, then packed in a tarball [Box Vagrant Format](https://developer.hashicorp.com/vagrant/docs/boxes/format).

# Usage

There are multiple Vagrant providers available:

* libvirt
* qemu


## libvirt

Install [`libvirt`](https://vagrant-libvirt.github.io/vagrant-libvirt/)
provider using the standard Vagrant plugin installation commnd:

```bash
vagrant plugin install vagrant-libvirt
```

Create a minimal `Vagrantfile` as follow:

```ruby
Vagrant.configure("2") do |config|
  config.vm.box = "cloud-image/<choose-a-distro>"
  config.vm.synced_folder ".", "/vagrant", disabled: true
end
```

Start Vagrant:

```bash
vagrant up --provider=libvirt
```

Here a more exaustive example (see [documentation](https://vagrant-libvirt.github.io/vagrant-libvirt/configuration.html) for more info):

```ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vagrant.plugins = "vagrant-libvirt"

  config.vm.box = "cloud-image/<choose-a-distro>"
  config.vm.synced_folder ".", "/vagrant", disabled: true
  #config.vm.synced_folder ".", "/vagrant", type: "nfs", mount_options: ["vers=3,tcp"]

  config.vm.provider :libvirt do |libvirt|
    libvirt.driver = "kvm"
    libvirt.uri = 'qemu:///system'
    #libvirt.socket = '/var/run/libvirt/libvirt-sock'
    #libvirt.host = 'localhost'
    #libvirt.username = ''
    #libvirt.password = ''
    #libvirt.id_ssh_key_file = "$HOME/.ssh/id_rsa"
  end

  config.vm.define :node do |libvirt|
    #libvirt.vm.network :forwarded_port, guest: 80, host: 4567
    #libvirt.vm.network :public_network, :dev => 'br0', :mode => 'bridge', :type => 'bridge'
    #libvirt.vm.network :public_network, :dev => 'br0', :mode => 'bridge', :type => 'bridge', :auto_config => false

    libvirt.vm.provider :libvirt do |domain|
      domain.memory = "1024"
      domain.cpus = "1"
      #domain.nested = true
      #domain.cpu_mode = 'host-passthrough'
      #domain.boot 'network'
      #domain.boot 'hd'
  
      #domain.storage :file, :size => '5G', :type => 'raw', :allow_existing => true
      #domain.storage :file, :device => 'cdrom', :path => '/mnt/linux.iso'
      #domain.graphics_type = 'none'
      #domain.graphics_port = 5901
      #domain.graphics_ip = '0.0.0.0'
    end

    #libvirt.vm.provision :shell, path: 'bootstrap.sh'
  end
end
```

## qemu

Install [`qemu`](https://github.com/ppggff/vagrant-qemu)
provider using the standard Vagrant plugin installation commnd:

```bash
vagrant plugin install vagrant-qemu
```

For an Apple Silicon, create a `Vagrantfile` as follow:

```ruby
Vagrant.configure("2") do |config|
  config.vagrant.plugins = "vagrant-qemu"

  config.vm.box = "cloud-image/debian-12"
  config.vm.synced_folder ".", "/vagrant", disabled: true

  config.vm.provider :qemu do |qemu|
    qemu.machine = "virt,accel=hvf,highmem=off"
    qemu.cpu = "cortex-a72"
    qemu.smp = "1"
    qemu.memory = "512M"
  end
end
```

Start Vagrant:

```bash
vagrant up --provider=qemu
```

# Vagrant Cloud Images

[//]: # (Do NOT edit the README.md file itself, edit the template file instead: ansible/templates/README.md.j2)

Purpose of this project is to provide [Vagrant Box images](https://app.vagrantup.com/cloud-image) based on public
colud images of various GNU/Linux distributions with no modifications at
all (or, at least, the minimum possible).

| distribution | vagrant box | support |
| ------------ | ----------- | ------- |
| AlmaLinux 10 | [cloud-image/almalinux-10](https://portal.cloud.hashicorp.com/vagrant/discover/cloud-image/almalinux-10) | May 2035 |
| AlmaLinux 9 | [cloud-image/almalinux-9](https://portal.cloud.hashicorp.com/vagrant/discover/cloud-image/almalinux-9) | May 2032 |
| AlmaLinux 8 | [cloud-image/almalinux-8](https://portal.cloud.hashicorp.com/vagrant/discover/cloud-image/almalinux-8) | Mar 2029 |
| Alpine Linux v3.23 | [cloud-image/alpine-3.23](https://portal.cloud.hashicorp.com/vagrant/discover/cloud-image/alpine-3.23) | Nov 2027 |
| Alpine Linux v3.22 | [cloud-image/alpine-3.22](https://portal.cloud.hashicorp.com/vagrant/discover/cloud-image/alpine-3.22) | May 2027 |
| Alpine Linux v3.21 | [cloud-image/alpine-3.21](https://portal.cloud.hashicorp.com/vagrant/discover/cloud-image/alpine-3.21) | Nov 2026 |
| Alpine Linux v3.20 | [cloud-image/alpine-3.20](https://portal.cloud.hashicorp.com/vagrant/discover/cloud-image/alpine-3.20) | Apr 2026 |
| Alpine Linux v3.19 | [cloud-image/alpine-3.19](https://portal.cloud.hashicorp.com/vagrant/discover/cloud-image/alpine-3.19) | Expired |
| Arch Linux | [cloud-image/arch-linux](https://portal.cloud.hashicorp.com/vagrant/discover/cloud-image/arch-linux) | undefined |
| CentOS Stream 10 | [cloud-image/centos-10](https://portal.cloud.hashicorp.com/vagrant/discover/cloud-image/centos-10) | Jan 2030 |
| CentOS Stream 9 | [cloud-image/centos-9](https://portal.cloud.hashicorp.com/vagrant/discover/cloud-image/centos-9) | May 2027 |
| CentOS Stream 8 | [cloud-image/centos-8](https://portal.cloud.hashicorp.com/vagrant/discover/cloud-image/centos-8) | Expired |
| CentOS 8 | [cloud-image/centos-8](https://portal.cloud.hashicorp.com/vagrant/discover/cloud-image/centos-8) | Expired |
| CentOS 7 | [cloud-image/centos-7](https://portal.cloud.hashicorp.com/vagrant/discover/cloud-image/centos-7) | Expired |
| Debian 13 (Trixie) | [cloud-image/debian-13](https://portal.cloud.hashicorp.com/vagrant/discover/cloud-image/debian-13) | August 2030 |
| Debian 12 (Bookworm) | [cloud-image/debian-12](https://portal.cloud.hashicorp.com/vagrant/discover/cloud-image/debian-12) | June 2028 |
| Debian 11 (Bullseye) | [cloud-image/debian-11](https://portal.cloud.hashicorp.com/vagrant/discover/cloud-image/debian-11) | June 2026 |
| Debian 10 (Buster) | [cloud-image/debian-10](https://portal.cloud.hashicorp.com/vagrant/discover/cloud-image/debian-10) | Expired |
| Fedora 43 | [cloud-image/fedora-43](https://portal.cloud.hashicorp.com/vagrant/discover/cloud-image/fedora-43) | Dec 2026 |
| Fedora 42 | [cloud-image/fedora-42](https://portal.cloud.hashicorp.com/vagrant/discover/cloud-image/fedora-42) | May 2026 |
| Fedora 41 | [cloud-image/fedora-41](https://portal.cloud.hashicorp.com/vagrant/discover/cloud-image/fedora-41) | Expired |
| Fedora 40 | [cloud-image/fedora-40](https://portal.cloud.hashicorp.com/vagrant/discover/cloud-image/fedora-40) | Expired |
| Fedora 39 | [cloud-image/fedora-39](https://portal.cloud.hashicorp.com/vagrant/discover/cloud-image/fedora-39) | Expired |
| openSUSE Leap 16.0 | [cloud-image/opensuse-leap-16.0](https://portal.cloud.hashicorp.com/vagrant/discover/cloud-image/opensuse-leap-16.0) | Oct 2027 |
| Rocky Linux 10 (Red Quartz) | [cloud-image/rocky-10](https://portal.cloud.hashicorp.com/vagrant/discover/cloud-image/rocky-10) | May 2035 |
| Rocky Linux 9 (Blue Onyx) | [cloud-image/rocky-9](https://portal.cloud.hashicorp.com/vagrant/discover/cloud-image/rocky-9) | May 2032 |
| Rocky Linux 8 (Green Obsidian) | [cloud-image/rocky-8](https://portal.cloud.hashicorp.com/vagrant/discover/cloud-image/rocky-8) | May 2029 |
| Ubuntu 26.04 LTS (Resolute Racoon) | [cloud-image/ubuntu-26.04](https://portal.cloud.hashicorp.com/vagrant/discover/cloud-image/ubuntu-26.04) | undefined |
| Ubuntu 24.04 LTS (Noble Numbat) | [cloud-image/ubuntu-24.04](https://portal.cloud.hashicorp.com/vagrant/discover/cloud-image/ubuntu-24.04) | April 2036 |
| Ubuntu 22.04 LTS (Jammy Jellyfish) | [cloud-image/ubuntu-22.04](https://portal.cloud.hashicorp.com/vagrant/discover/cloud-image/ubuntu-22.04) | April 2034 |
| Ubuntu 20.04 LTS (Focal Fossa) | [cloud-image/ubuntu-20.04](https://portal.cloud.hashicorp.com/vagrant/discover/cloud-image/ubuntu-20.04) | April 2032 |
| Ubuntu 18.04 LTS (Bionic Beaver) | [cloud-image/ubuntu-18.04](https://portal.cloud.hashicorp.com/vagrant/discover/cloud-image/ubuntu-18.04) | April 2030 |
| Ubuntu 16.04 LTS (Xenial Xerus) | [cloud-image/ubuntu-16.04](https://portal.cloud.hashicorp.com/vagrant/discover/cloud-image/ubuntu-16.04) | April 2028 |
| Ubuntu 14.04 LTS (Trusty Tahr) | [cloud-image/ubuntu-14.04](https://portal.cloud.hashicorp.com/vagrant/discover/cloud-image/ubuntu-14.04) | April 2026 |

## cloud-init injection

This method consists to inject a `cloud-init` configuration file under
`/etc/cloud/cloud.cfg.d/99_vagrant.cfg` with the following content:

```yaml
datasource_list: [ NoCloud, None ]
ssh_pwauth: False
ssh_authorized_keys:
  # https://github.com/hashicorp/vagrant/tree/master/keys
  - 'ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA6NF8iallvQVp22WDkTkyrtvp9eWW6A8YVr+kz4TjGYe7gHzIw+niNltGEFHzD8+v1I2YJ6oXevct1YeS0o9HZyN1Q9qgCgzUFtdOKLv6IedplqoPkcmF0aYet2PkEDo3MlTBckFXPITAMzF8dJSIFo9D8HfdOV0IAdx4O7PtixWKn5y2hMNG0zQPyUecp4pzC6kivAIhyfHilFR61RGL+GPXQ2MWZWFYbAGjyiYJnAmCP3NOTd0jMZEnDkbUvxhMmBYSdETk1rRgm+R4LOzFUGaHqHDLKLX+FIPKcF96hrucXzcWyLbIbEgE98OHlnVYCzRdK8jlqm8tehUc9c9WhQ== vagrant insecure public key'
users:
  # Preserve default distro user
  - default
  # Create Vagrant user with disabled password
  - name: vagrant
    plain_text_passwd: vagrant
    doas: ["permit nopass vagrant"]
    sudo: ["ALL=(ALL) NOPASSWD:ALL"]
    shell: /bin/sh
    lock_passwd: true
    ssh_authorized_keys:
      # https://github.com/hashicorp/vagrant/tree/master/keys
      - 'ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA6NF8iallvQVp22WDkTkyrtvp9eWW6A8YVr+kz4TjGYe7gHzIw+niNltGEFHzD8+v1I2YJ6oXevct1YeS0o9HZyN1Q9qgCgzUFtdOKLv6IedplqoPkcmF0aYet2PkEDo3MlTBckFXPITAMzF8dJSIFo9D8HfdOV0IAdx4O7PtixWKn5y2hMNG0zQPyUecp4pzC6kivAIhyfHilFR61RGL+GPXQ2MWZWFYbAGjyiYJnAmCP3NOTd0jMZEnDkbUvxhMmBYSdETk1rRgm+R4LOzFUGaHqHDLKLX+FIPKcF96hrucXzcWyLbIbEgE98OHlnVYCzRdK8jlqm8tehUc9c9WhQ== vagrant insecure public key'
```

Packer is not used at all. The disk image are downloaded, mounted, injected, then packed in a [Box Vagrant Format](https://developer.hashicorp.com/vagrant/docs/boxes/format) tarball. That ensure the creation of Vagrant user during the first boot by the `cloud-init` service included in every GNU/Linux cloud images.

Refer to [Vagrant documentation](https://developer.hashicorp.com/vagrant/docs/cloud-init) and [cloud-init documentation](https://docs.cloud-init.io/en/latest/reference/examples.html) for more information on how to use `cloud_init` block inside `Vagrantfile`:

```ruby
# Use bash as default shell for Vagrant user and enable SSH password authentication
# WARNING: do not use "users:" to avoid overwrite 99_vagrant.cfg
config.vm.cloud_init do |cloud_init|
  cloud_init.content_type = "text/cloud-config"
  cloud_init.inline = <<-EOF
    timezone: Europe/Rome
    package_update: True
    packages:
      - bash
    runcmd:
      - chsh -s /bin/bash vagrant
      - passwd -u vagrant
    ssh_pwauth: True
  EOF
end
```

```ruby
# Change Vagrant user password and enable SSH authentication
# WARNING: do not use "users:" to avoid overwrite 99_vagrant.cfg
config.vm.cloud_init do |cloud_init|
  cloud_init.content_type = "text/cloud-config"
  cloud_init.inline = <<-EOF
    timezone: Europe/Rome
    chpasswd:
      expire: False
      users:
        - name: vagrant
          password: N3wP4ssw0rd
          type: text
    ssh_pwauth: True
  EOF
end
```

# Usage

There are multiple Vagrant providers available:

* virtualbox
* libvirt
* qemu


## virtualbox

```bash
vagrant init cloud-image/<choose-a-distro>
vagrant up
```


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
  #config.vm.synced_folder ".", "/vagrant", type: "nfs", nfs_udp: false

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
provider using the standard Vagrant plugin installation command:

```bash
vagrant plugin install vagrant-qemu
```

For an Apple Silicon, create a `Vagrantfile` as follow:

```ruby
Vagrant.configure("2") do |config|
  config.vagrant.plugins = "vagrant-qemu"

  config.vm.box = "cloud-image/<choose-a-distro>"
  config.vm.synced_folder ".", "/vagrant", disabled: true

  config.vm.provider :qemu do |qemu|
    qemu.machine = "virt,accel=hvf,highmem=off"
    qemu.cpu = "max"
    qemu.smp = "2"
    qemu.memory = "1024M"
  end
end
```

To run an x86_64 distro on an Apple Silicon:

```ruby
Vagrant.configure("2") do |config|
  config.vagrant.plugins = "vagrant-qemu"

  config.vm.box = "cloud-image/<choose-a-distro>"
  config.vm.box_architecture = "amd64"
  config.vm.synced_folder ".", "/vagrant", disabled: true

  config.vm.provider :qemu do |qemu|
    qemu.arch = "x86_64"
    qemu.machine = "q35"
    qemu.cpu = "max"
    qemu.smp = "cpus=2,sockets=1,cores=2,threads=1"
    qemu.net_device = "virtio-net-pci"
    qemu.extra_qemu_args = %w(-accel tcg,thread=multi,tb-size=512)
  end
end
```

Start Vagrant:

```bash
vagrant up --provider=qemu
```

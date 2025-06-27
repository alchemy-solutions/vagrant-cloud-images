# Vagrant Cloud Images

Purpose of this project is to provide [Vagrant Box images](https://app.vagrantup.com/cloud-image) based on public
colud images of various GNU/Linux distributions with no modifications at
all (or, at least, the minimum possible).

| distribution | version | vagrant box | support |
| ------------ | :-----: | ----------- | ------- |
| AlmaLinux | 10 | cloud-image/almalinux-10 | May 2035 |
| AlmaLinux | 9 | cloud-image/almalinux-9 | May 2032 |
| AlmaLinux | 8 | cloud-image/almalinux-8 | Mar 2029 |
| Alpine Linux | 3.22 | cloud-image/alpine-3.22 | May 2027 |
| Alpine Linux | 3.21 | cloud-image/alpine-3.21 | Nov 2026 |
| Alpine Linux | 3.20 | cloud-image/alpine-3.20 | Apr 2026 |
| Alpine Linux | 3.19 | cloud-image/alpine-3.19 | Nov 2025 |
| CentOS Stream | 10 | cloud-image/centos-10-stream | Jan 2030 |
| CentOS Stream | 9 | cloud-image/centos-9-stream | May 2027 |
| CentOS Stream | 8 | cloud-image/centos-8-stream | Expired |
| CentOS | 8 | cloud-image/centos-8 | Expired |
| CentOS | 7 | cloud-image/centos-7 | Expired |
| Debian | 12 | cloud-image/debian-12 | Jun 2028 |
| Debian | 11 | cloud-image/debian-11 | Aug 2026 |
| Fedora | 42 | cloud-image/fedora-42 | May 2026 |
| Fedora | 41 | cloud-image/fedora-41 | Nov 2025 |
| Fedora | 40 | cloud-image/fedora-40 | Expired |
| Fedora | 39 | cloud-image/fedora-39 | Expired |
| Fedora | 38 | cloud-image/fedora-38 | Expired |
| openSUSE Leap | 15.6 | cloud-image/opensuse-leap-15.6 | Dec 2025 |
| Ubuntu | 24.04 | cloud-image/ubuntu-24.04 | Apr 2036 |
| Ubuntu | 22.04 | cloud-image/ubuntu-22.04 | Apr 2034 |
| Ubuntu | 20.04 | cloud-image/ubuntu-20.04 | Apr 2032 |
| Ubuntu | 18.04 | cloud-image/ubuntu-18.04 | Apr 2030 |
| Ubuntu | 16.04 | cloud-image/ubuntu-16.04 | Apr 2028 |
| Ubuntu | 14.04 | cloud-image/ubuntu-14.04 | Apr 2026 |

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

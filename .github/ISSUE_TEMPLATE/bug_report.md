---
name: Bug report
about: Create a report to help us improve
title: ''
labels: ''
assignees: ''

---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '...'
3. Scroll down to '...'
4. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Please complete the following information:**
 - Host OS and Version: [e.g. Debian 13, macOS 26, Windows 11]
 - Vagrant Version: [e.g. 2.4.9]
 - Vagrant Provider: [e.g. virtualbox, qemu, libvirt]
 - Vagrant Box and Version: [e.g. cloud-image/ubuntu-18.04 20230607.0.1]

**Vagrantfile**
Share the file remembering to remove any sensitive data:
```ruby
# e.g.
Vagrant.configure("2") do |config|
  config.vm.box = "cloud-image/rocky-10"
  config.vm.box_architecture = "amd64"
  config.vm.provider :qemu do |qemu|
    qemu.machine = "virt,accel=tcg,highmem=off"
    qemu.cpu = "max"
  end
end
```

**Additional context**
Add any other context about the problem here.

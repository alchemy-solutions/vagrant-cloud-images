# Build

## Overview
This repository builds Vagrant Cloud images using the `build.sh` script. It supports filtering by distro, architecture, provider, and custom patch selection.

## Prerequisites
- Bash 5.0+
- `qemu-img` and `libguestfs-tools` or `docekr` installed
- `VAGRANT_CLOUD_TOKEN` environment variable set

## Quick Start
```bash
./build.sh
```

### Override Variables
Use `-e` to set a variable:
```bash
./build.sh -e filter_distro=centos -e filter_arch=arm64 -e preserve=true -e upload=false
```

## Environment Variables
| Variable          | Description |
|-------------------|-------------|
| `filter_distro`   | Target distribution (e.g., `centos`, `ubuntu`) |
| `filter_release`  | Release channel (`trusty`, `18.04`, ...) |
| `filter_arch`     | Target architecture (`x86_64`, `arm64`) |
| `filter_provider` | Provider to target (`virtualbox`, `qemu`, `libvirt`) |
| `overwrite`       | Delete existing image before building (`true` / `false`) |
| `preserve`        | Keep intermediate artifacts after build (`true` / `false`) |
| `upload`          | Push the built image to Vagrant Cloud (`true` / `false`) |

## Troubleshooting
- `guestfish: command not found` – install the required packages (`libguestfs-tools`).
- `VAGRANT_CLOUD_TOKEN` not set – export it: `export VAGRANT_CLOUD_TOKEN=your_token`.
- Image not uploading – check network connectivity and token scopes.

## Contributing
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/foo`).
3. Implement, test, and ensure lint and tests pass.
4. Open a Pull Request with a clear description.

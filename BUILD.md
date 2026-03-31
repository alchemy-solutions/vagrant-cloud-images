# Build

```shell
./build.sh
```

## Filter

### Distro

```shell
./build.sh -e filter_distro=centos
```

```
./build.sh -e filter_release=trusty -e overwrite=true -e filter_arch=arm64 -e filter_provider=virtualbox -e preserve=true -e upload=false -e cloud_image_patch=1
```

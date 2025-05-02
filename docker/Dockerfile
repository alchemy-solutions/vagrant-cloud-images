FROM debian

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
 && apt-get -y install \
	libguestfs-tools

#ENTRYPOINT ["/usr/bin/guestfish"]
# docker run -it --privileged --rm --name guestfish --workdir /build -v "${PWD}:/build" guestfish --rw -a disk.raw -i

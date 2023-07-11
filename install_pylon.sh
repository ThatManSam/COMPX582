#!/bin/bash

check_response() {
    if [[ $? -ne 0 ]]; then
        echo "Error running $1"
        exit 1
    fi
}

platform=$(uname -m)

if [[ "$platform" == "arm64" || "$platform" == "aarch64" ]]; then
# if [[ "$platform" == "aarch64" ]]; then
    URL=https://www.baslerweb.com/fp-1668420816/media/downloads/software/pylon_software/pylon_7.2.1.25747_aarch64_debs.tar.gz
else
    URL=https://www.baslerweb.com/fp-1668420813/media/downloads/software/pylon_software/pylon_7.2.1.25747_x86_64_deps.tar.gz
fi

echo "/Downloading Pylon for $platform from $URL"
curl -L -v $URL -H "Content-Type: application/x-gzip" --output pylon.tar.gz
check_response "Pylon Download"

echo "/Extracting files"
tar -xf pylon.tar.gz
check_response "Extracting Files"

echo "/Installing .deb packages"
dpkg -i ./pylon*.deb
check_response "Installing .deb packages"

echo "/Running setup script"
/opt/pylon/bin/pylon-setup-env.sh
check_response "Setup script"
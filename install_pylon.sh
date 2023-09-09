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
    URL=https://www.baslerweb.com/fp-1668420813/media/downloads/software/pylon_software/pylon_7.2.1.25747_x86_64_debs.tar.gz
fi

DOWNLOAD_FILE=pylon.tar.gz

echo "/Downloading Pylon for $platform from $URL"
curl -L $URL -H "Content-Type: application/x-gzip" --output $DOWNLOAD_FILE
check_response "Pylon Download"

echo "/Extracting files"
tar -xf $DOWNLOAD_FILE
check_response "Extracting Files"

echo "/Installing .deb packages"
sudo dpkg -i ./pylon*.deb
check_response "Installing .deb packages"

echo "/Running setup script"
/opt/pylon/bin/pylon-setup-env.sh
check_response "Setup script"

echo "Cleaning up files"
rm -f $DOWNLOAD_FILE pylon*.deb codemeter*.deb INSTALL
check_response "Removing Files"
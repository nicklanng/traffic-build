#!/bin/bash

if [ $(id -u) -ne 0 ]; then echo "Please run as root"; exit; fi

cd /usr/local/bin
sudo git clone https://github.com/nicklanng/traffic-build
cd traffic-build
sudo pip3 install requests-2.13.0-py2.py3-none-any.whl

sudo chmod 755 /usr/local/bin/traffic-build/main.py

sudo cp trafficbuild.sh /etc/init.d
sudo chmod 755 /etc/init.d/trafficbuild.sh
sudo update-rc.d trafficbuild.sh defaults
sudo /etc/init.d/trafficbuild.sh start

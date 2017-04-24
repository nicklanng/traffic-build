#!/bin/bash

if [ "$EUID" -ne 0 ]; then echo "Please run as root"; exit; fi

cd /usr/local/bin
git clone https://github.com/nicklanng/traffic-build
cd traffic-build
pip3 install requests-2.13.0-py2.py3-none-any.whl

chmod +x /usr/local/bin/traffic-build/main.py

cp trafficlights.sh /etc/init.d
chmod +x /usr/local/bin/traffic-build/trafficbuild.sh
update-rc.d trafficbuild.sh defaults
/etc/init.d/trafficbuild.sh start

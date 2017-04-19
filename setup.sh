#!/bin/bash

cd /home/$USER
git clone https://github.com/nicklanng/traffic-build
cd traffic-build
pip3 install requests-2.13.0-py2.py3-none-any.whl

(crontab -l ; echo "@reboot ./home/$USER/traffic-build/launcher.sh >/var/logs/traffic-build 2>&1")| crontab -

./home/$USER/traffic-build/launcher.sh >/var/logs/traffic-build 2>&1 &

#!/bin/bash

echoNeedInstall()
{
   echo "########################################################################"
   echo " Installing $1"
   echo "########################################################################"
}

if ! which pip3 >/dev/null; then
   echoNeedInstall pip3
   sudo apt-get install python3-pip python3-dev
fi

if ! which virtualenv >/dev/null; then
   echoNeedInstall virtualenv
   sudo apt-get install python-virtualenv
fi

if ! which curl >/dev/null; then
   echoNeedInstall curl
   sudo apt-get install curl
fi

# clean, create and activate the virtual env
sudo rm -R venv
virtualenv --python=/usr/bin/python3 --system-site-packages venv
. venv/bin/activate
# install dependencies
pip install -r requirements.txt --upgrade --force-reinstall

# deactivate virtual env
deactivate

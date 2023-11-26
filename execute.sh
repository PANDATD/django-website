#!/usr/bin/bash

echo "udpated packages"
sudo apt update -y 
echo "installing dependancies"
pip3 install -r requirements.txt

python3 manage.py runserver 


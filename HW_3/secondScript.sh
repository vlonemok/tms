#!/bin/bash

sudo useradd -m $1

touch /home/$1/systemInformation

uname -r >> /home/$1/systemInformation
echo '##############################' >>/home/$1/systemInformation

lscpu >> /home/$1/systemInformation
echo '##############################' >>/home/$1/systemInformation

free -h >> /home/$1/systemInformation
echo '##############################' >>/home/$1/systemInformation

df >>/home/$1/systemInformation

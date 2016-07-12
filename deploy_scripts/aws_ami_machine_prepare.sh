!# /bin/bash

# make a docker ready machine with a vanilla Ubuntu 14.04 machine from aws

# install docker
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates
sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
echo deb https://apt.dockerproject.org/repo ubuntu-trusty main > ./docker.list
sudo mv ./docker.list /etc/apt/sources.list.d/docker.list
sudo apt-get update
sudo apt-get purge lxc-docker
apt-cache policy docker-engine
sudo apt-get update
sudo apt-get install -y linux-image-extra-$(uname -r)
sudo apt-get update
sudo apt-get install -y docker-engine=1.11.2-0~trusty

# install pip
apt-get install -y python-pip

#install docker-compose #TODO I don't need compose in deployment.
sudo pip install docker-compose==1.7.1

#install unzip
sudo apt-get install -y unzip

# install the CodeDeploy Agent
sudo apt-get update
sudo apt-get install ruby2.0
sudo apt-get install wget
cd /home/ubuntu
wget https://bucket-name.s3.amazonaws.com/latest/install
chmod +x ./install
sudo ./install auto

sudo reboot

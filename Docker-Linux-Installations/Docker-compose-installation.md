On desktop systems like Docker for Mac and Windows, Docker Compose is included as part of those desktop installs.

For Linux machines follow this process



Step1: Download
Download docker-compose latest from the url

https://github.com/docker/compose/releases/


https://github.com/docker/compose/releases/download/1.22.0-rc2/docker-compose-Linux-x86_64



Rename to docker-compose and move to  /usr/local/bin/docker-compose

Apply executable permissions to the binary:

 From the dir
chmod +x ./docker-compose

Move the binary in to your PATH.

sudo mv ./docker-compose /usr/local/bin/docker-compose

OR use curl to download the latest version by 
using the latest Compose release number in the download command.

sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose


 

Step 2
Apply executable permissions to the binary:

sudo chmod +x /usr/local/bin/docker-compose


Step3
Test the installation.
docker-compose --version
-->docker-compose version 1.21.2, build 1719ceb

1. sudo apt install docker-compose

1. sudo apt remove docker-compose

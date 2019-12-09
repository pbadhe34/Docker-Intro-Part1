 


On macOS and Windows, Docker-Machine is installed along with other Docker products when you install the Docker for Mac, Docker for Windows, or Docker Toolbox.

Step1 : Download for linux machines directly
install the Machine binaries directly  from

https://github.com/docker/machine/releases

https://github.com/docker/machine/releases/download/v0.15.0/docker-machine-Linux-x86_64

https://github.com/docker/machine/releases/download/v0.15.0/docker-machine-Linux-x86_64

Rename to docker-machine

Apply executable permissions to the binary:

 From the dir
chmod +x ./docker-machine

Move the binary in to your PATH.

sudo mv ./docker-machine /usr/local/bin/docker-machine


OR
Download with CURL
$ base=https://github.com/docker/machine/releases/download/v0.14.0 && curl -L $base/docker-machine-$(uname -s)-$(uname -m) >/tmp/docker-machine && sudo install /tmp/docker-machine /usr/local/bin/docker-machine

Step 2
Apply executable permissions to the binary:

sudo chmod +x /usr/local/bin/docker-machine

Step3
Test the installation.

docker-machine version

docker-machine create --driver virtualbox default

************************************************************************************************

Install proper version of VM Manager

To check the kernel module versuin
uname -r

4.13.0-45-generic

To remove existing VBox
sudo apt remove virtualbox virtualbox-5.*

sudo apt-get install virtualbox

vboxmanage --version  -->5.1.34_Ubuntur121010

The latest versioin has  issues with strting the VM
 

1. sudo apt-get --reinstall install virtualbox-dkms

2. sudo apt-get install -f 


3. Read the VirtualBox version
   vboxmanage --version
**************************************************************************************************
Solution for VirtualBox not starting the VM in SecureBoot mode

gorka.eguileor.com/vbox-vmware-in-secureboot-linux

Error Details

The vboxdrv kernel module is not loaded. Either there is no module
available for the current kernel (3.15.8-200.fc20.x86_64) or it failed to
load. Please recompile the kernel module and install it by sudo /etc/init.d/vboxdrv setup

You will not be able to start VMs until this problem is fixed.


 Seems if SecureBoot in enabled in the machine's BIOS then Ubuntu enforces the signing chain of bootloader, kernel and kernel modules. This, I assume, is what is causing modprobe to fail when installing the virtualbox kernel modules.

Check out the Ubuntu's SecurityTeam SecureBoot page for more information including potential workarounds. I would post the link but I just signed up and can't post links yet. Should be the first result in google for ubuntu SecurityTeam SecureBoot.

We took the easy way out and just disabled SecureBoot and everything works fine now. 

going to BIOS settings and completely disabling Secure Boot and enabling the legacy boot option

**********************************************************************************************





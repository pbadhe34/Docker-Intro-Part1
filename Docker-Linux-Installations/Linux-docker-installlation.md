https://kubernetes.io/docs/setup/production-environment/container-runtimes/#docker
 
  sudo subscription-manager  register

   sudo subscription-manager attach

   sudo yum update

   Remove earlier versions if any

  sudo yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine

 
sudo yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2  
  

 sudo yum install selinux-policy selinux-policy-base selinux-policy-targeted  

  sudo yum list     
   
  sudo yum info selinux-policy

  sudo yum info selinux-policy-base
  
  sudo yum info selinux-policy-targeted


 The Centos repoistory
http://mirror.centos.org/centos/7/extras/x86_64/Packages/
   
   sudo yum install -y http://mirror.centos.org/centos/7/extras/x86_64/Packages/container-selinux-2.107-3.el7.noarch.rpm

   yum info container-selinux

  Set up the repository

   sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo


  Install Docker Engine - Community
   sudo yum install docker-ce docker-ce-cli containerd.io

 
   Start Docker.

  sudo systemctl start docker


  sudo systemctl status docker

  sudo systemctl stop docker

  sudo systemctl restart docker

  sudo systemctl status containerd

 >docker info
>docker version

  >docker run hello-world

   Manage Docker as a non-root user

  The Docker daemon binds to a Unix socket instead of a TCP port. By default that Unix socket is owned by the user root and other users can only access it using sudo. The Docker daemon always runs as the root user.

  To run docker commands need sudo acess

  To be able to manage docker as non-root user

   create a Unix group called docker and add users to it. 
 When the Docker daemon starts, it creates a Unix socket accessible by members of the docker group.


   1.Create the docker group.

   sudo groupadd docker

   2. Add your user to the docker group.

   sudo usermod -aG docker Prakash


 3. Log out and log back in so that your group membership is re-evaluated.

If testing on a virtual machine, it may be necessary to restart the virtual machine for changes to take effect.

On a desktop Linux environment such as X Windows, log out of your session completely and then log back in.

On Linux, you can also run the following command to activate the changes to groups without logOut:
  >newgrp docker 

  Configure Docker to start on boot

Most current Linux distributions (RHEL, CentOS, Fedora, Ubuntu 16.04 and higher) use systemd to manage which services start when the system boots. Ubuntu 14.10 and below use upstart.
 
 
  sudo systemctl enable docker  

 OR
  sudo chkconfig docker on


  4.Verify that you can run docker commands without sudo.

    docker run hello-world

  Note
  If you initially ran Docker CLI commands using sudo before adding your user to the docker group, you may see the following error, which indicates that your ~/.docker/ directory was created with incorrect permissions due to the sudo commands.
 WARNING: Error loading config file: /home/user/.docker/config.json -
stat /home/user/.docker/config.json: permission denied

  To fix this problem, either remove the ~/.docker/ directory (it is recreated automatically, but any custom settings are lost), or change its ownership and permissions using the following commands:

  sudo chown "$USER":"$USER" /home/"$USER"/.docker -R
  sudo chmod g+rwx "$HOME/.docker" -R



  Use a different storage engine

  The default storage engine and the list of supported storage engines depend on your host’s Linux distribution and available kernel drivers.


  Configure default logging driver

Docker provides the capability to collect and view log data from all containers running on a host via a series of logging drivers. 
 The default logging driver, json-file, writes log data to JSON-formatted files on the host filesystem. Over time, these log files expand in size, leading to potential exhaustion of disk resources. 
 To alleviate such issues, either configure an alternative logging driver such as Splunk or Syslog, or set up log rotation for the default driver. If you configure an alternative logging driver,   


   sudo ls /var/lib/docker/containers



  https://docs.docker.com/config/containers/logging/dual-logging/

  https://docs.docker.com/storage/storagedriver/select-storage-driver/

https://docs.docker.com/storage/volumes/

  https://docs.docker.com/storage/volumes/#use-a-volume-driver

  Docker daeom cnfiguartion
  Docker config with Proxies


******************************************************************************

Docker-compose instalation

  sudo curl -L https://github.com/docker/compose/releases/download/1.25.0-rc2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

  sudo chmod +x /usr/local/bin/docker-compose  

  docker-compose version


 ******************************************************************************************************

 Docker-Machine installation

  sudo curl -L https://github.com/docker/machine/releases/download/v0.16.2/docker-machine-`uname -s`-`uname -m` >/tmp/docker-machine
    
    sudo chmod +x /tmp/docker-machine
    sudo cp /tmp/docker-machine /usr/local/bin/docker-machine

  docker-machine version

  docker-machine ls







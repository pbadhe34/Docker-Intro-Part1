 
  Check wheteher docker is running
  docker info

 OR to display the docker running processes
 docker ps

To display active docker processes:
docker ps -a

 To run an image in intercative(attached) mode

 docker run -it ubuntu bash

*****************************////*************************

 To run apache httpd image in container  in intercative and detached mode 

docker run -dit --name my-apache-app httpd:2.4

Chevk the container IP
docker inspect my-apache-app 

Run in the browser'
http://<container-ip>:80

 Stop it
docker stop my-apache-app 

Remove the container
docker rm my-apache-app 

*************************
To run apache httpd in container  
docker run -dit --name my-apache-app httpd 

***************************************

To run apache httpd in container with host port mapping
docker run -dit --name my-apache-app -p 8090:80 httpd 


***********************************************
To run apache httpd in container with html files mapped to httpd from current dir and hpost port mapping
The  $(pwd)/public to refer to   local public html file folder

docker run -dit --name apache-app -p 8090:80 --mount src="$(pwd)/public",target=/usr/local/apache2/htdocs,type=bind  httpd:2.4

****************************************
 


  To build the custom image
  Change to the application direcory is current user path

Build with default Dockerfile in current directory
    cd ..
Build the image with name as apache  from Dockerfile
  docker build -t apache .


  *******************************

 Build from file 'Dockerfile-Apache-Server' and tag  the image as 'apache-server'


 docker build -f./Dockerfile-Apache-Server -t apache . 

   ************************

To Run the app-image in detacheed mode
  docker run -d apache
 
  docker images ls
  

  To Run the app-image in detacheed mode
  docker run -d apache-server

 
  Run with host name in detached mode
  docker run -d -h my-host apache-server

  Run with container and host name assigned
 docker run -d --name my_container -h py-host apache-server

To make this app available outside the docker container with mapping to host address space,the port 80 must be available on host machine

   docker run -d -h my-host  --network host apache

   Run the apache-server with host port attached to docker container
To run the app by mapping the current machine’s port 4000 to the container’s published port 80 using -p:
  
 Map the container port 80 to Docker Host port as 4000

 docker run -d -p 4000:80 -h my-host apache

curl http://localhost:4000

 
Map to local host address space
docker run -d -p 127.0.0.1:3500:80 -h my-host apache
curl http://127.0.0.1:3500

Mapping to physical IP address is possibkle with Linux Bare metal host 

docker run -d -p 192.168.99.1:3600:80 -h my-host apache

curl http://192.168.99.1:3600

*****************************
binding to the docker host's 127.0.0.1. When the docker host is in a VM, that's different from the external 127.0.0.1 on the system. 

**********************************

docker ps

docker run -d -p 192.168.0.100:3200:80 --name my_container -h my-host apache

curl http://192.168.0.100:3200


Map to the machine addreess
docker run -d -p 192.168.99.100:3200:80 --name my_container -h my-host apache-server

curl http://192.168.99.100:3200

***********************************************************
Execute process inside the conatiner
docker exec -it <container name> <command> to execute whatever command you specify in the container.

docker attach will let you connect to your Docker container, but this isn't really the same thing as ssh. If your container is running a webserver, for example, docker attach will probably connect you to the stdout of the web server process. It won't necessarily give you a shell.


docker attach my_container : dipsly the container log continuusly on stdOut terminal.

start a shell to connect to the container;

docker exec -it e249327a386b /bin/bash
cat /etc/hosts
pwd
history
hostname -I 
hostname


docker exec -it  $(docker ps -q) bash: works on last conatiner created

Export the environmental variables from the running container

docker exec -i -t $(docker ps -l -q) env   

Add -q to automatically parse and return the last CID created.

To read the conrainer ip addresses

docker inspect --format '{{ .NetworkSettings.IPAddress }}' $(docker ps -q)
172.17.0.1
 

docker attach my-container

Attach to STDIN/STDOUT/STDERR (-a)
The -a flag tells docker run to bind to the container’s STDIN, STDOUT or STDERR.  

***************************************************
To work with PHP apache image

docker run --rm -p 8200:80 -v "$PWD":/var/www/html php:7.0-apache

 

 To Run a single php script
 docker run -it --rm --name my-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp php:7.0-cli php home.php



******************************************************************************************************
 

 

 docker network inspect bridge
 docker network inspect host

 docker top CONTAINER-Name [ps OPTIONS]: To Display the running processes of a container

  docker top	my_container

  docker top	my_container <process-pid>


  docker port my_container

*************************************

  docker-machine ip 

  curl http://192.168.99.100:4000

*********************************
  docker ps

 docker container ls  

 docker container ls -a

  The app is running on :http://192.168.99.100:4000  
  
To see the docker container choosen port. 
Access is then possible via localhost:port.

docker port <container id/name>

   
  curl http://192.168.99.100:4000

  docker ps

  docker logs my_container

 docker inspect my_container


docker inspect my_container | grep "IPAddress"

docker inspect my_container | grep '"IPAddress"' | head -n 1

docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' my_container

 
To get all container names and their IP addresses in just one single command.

docker inspect -f '{{.Name}} - {{.NetworkSettings.IPAddress }}' $(docker ps -aq)

Show all containers IP addresses:

docker inspect --format='{{.Name}} - {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps -aq)

The Docker creates three networks automatically.
 You can list these networks using the docker network ls command:

docker network ls

Unless configured Docker, Docker always launches the containers in the bridge network. 
So you can try this command below:

docker network inspect bridge

The default netwwork type creatred bt docker is bridge

  To specify network option :
docker run --network=<NETWORK> 
Docker daemon connects containers to this network.The default is bridge.


 To run with host network without port mapping
assign the host IP to container ?


docker run -d --name my_container -h my-host --network host test-app:v1 :  

Run without host name mapping

docker run -d --name my_container --network host test-app:v1
 

curl http://192.168.99.100:8090/

Add entries to container hosts file (–add-host)
You can add other hosts into a container’s /etc/hosts file by using one or more --add-host flags. This example adds a static address for a host named user-host:

docker run -d --add-host=user-host:192.168.0.100 --rm -it pbadhe34/my-apps:app1

  
The Python is serving your app at http://0.0.0.0:80. But that message is coming from inside the container, which doesn’t know you mapped port 80 of that container to 4000, making the correct URL http://localhost:4000.

   To check the list of containers running

   docker container ls
   
   Container ID with docker image is displayed

********************
   To stop the cotainer

   docker stop <container-id/name>

  docker pause <container-id/name>

  docker start <container-id/name>


  docker rm <container-id/name>

 ***********************************************
  Log in to the Docker private  registry on your local machine.

  docker login

  Publish the image on docker hub in the format
  docker tag image username/repository:tag

 docker tag test-app pbadhe34/my-apps:app1
 
  docker images
  docker images ls

  To Publish the image to docker hub
  Upload your tagged image to the repository:

  docker push pbadhe34/my-apps:app1

Pull and run the image from the remote repository
From now on, you can use docker run and run your app on any machine with this command in the format
docker run -p 4000:8090 username/repository:tag

docker run -d -p 3000:8090 pbadhe34/my-apps:app1

 If the image isn’t available locally on the machine, Docker will pull it from the repository.

To get the redis working with HitCounter

 docker run -d --name redis -h redis redis

 If you don’t specify the :tag portion of these commands, the tag of :latest will be assumed, both when you build and when you run images. Docker will use the last version of the image that ran without a tag specified (not necessarily the most recent image).

List images by name and tag
docker images test-app

List the full length image IDs
docker images --no-trunc

Format the image output
docker images --format "{{.ID}}: {{.Repository}}"

docker images test-app --format "{{.ID}}: {{.Repository}}"

docker images --format "table {{.ID}}\t{{.Repository}}\t{{.Tag}}"
 
List all exited containers
docker ps -aq -f status=exited

Remove stopped containers
docker ps -aq --no-trunc | xargs docker rm


Remove dangling/untagged images
docker images -q --filter dangling=true | xargs docker rmi

Remove containers created after a specific container
docker ps --since <container name/id> -q | xargs docker rm

Remove containers created before a specific container
docker ps --before <container name/id> -q | xargs docker rm

Use --rm together with docker build to remove intermediary images during the build process.

Use --rm for docker build


To remove the images

docker rmi <image name>

docker rmi py-app:v1

docker rmi py-app:latest


docker rmi test-app

Running the commands within the container

The container name/id can be used as containerId in "exec" or "rm" command. When you want to run command in an existing container(running or exited), you will use "docker exec" command in which you specify container name or id.
 

create a container named app_cont with image(ubuntu ) and start a process "sleep" 1 minutes then exit.

 Run in detached mode
docker run -d --name app_cont ubuntu sleep 60

docker ps

Run another command in the container app_cont 

docker exec app_cont ps -aef

UID        PID  PPID  C STIME TTY          TIME CMD
root         1     0  0 04:21 ?        00:00:00 sleep 60
root        11     0  3 04:21 ?        00:00:00 ps -aef

Delete the container app_cont

docker stats  app_cont

docker stats  app_cont --format "table {{.ID}}\t{{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}"

docker stats  --all --format "table {{.ID}}\t{{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}"



docker stop app_cont 

docker start app_cont 


docker pause app_cont
docker unpause app_cont 


docker rm app_cont 

Run the container in  interactive shell  
# allocate a tty, attach stdin and stdout
# To detach the tty without exiting the shell,
# use the escape sequence Ctrl-p + Ctrl-q
# note: This will continue to exist in a stopped state once exited (see "docker ps -a")

docker run -i -t --name container1 busybox


Automatically remove the container when it exits

docker run -d --rm --name app_cont ubuntu sleep 10

docker node ls

docker node ls --format "{{.ID}}: {{.Hostname}} {{.TLSStatus}}"

docker system info	-->Display system-wide information

docker system df	--> Show docker disk usage

docker system events	-->Get real time events from the server

docker system prune	-->Remove unused data


docker images -f dangling=true

docker rmi $(docker images -f dangling=true -q)

Removing images according to a pattern

docker images | grep "pattern" | awk '{print $1}' | xargs docker rm


All the Docker images on a system can be listed by adding -a to the docker images command. 
docker images -a
Once you're sure you want to delete them all, you can add the -q flag to pass the Image ID to docker rmi:

docker rmi $(docker images -a -q)

find all the images that match a pattern using a combination of docker images and grep. Once you're satisfied, you can delete them by using awk to pass the IDs to docker rmi. Note that these utilities are not supplied by Docker and are not necessarily available on all systems:

docker ps -a |  grep "pattern"

To Remove a container upon exit

If you know when you’re creating a container that you won’t want to keep it around once you’re done, you can run docker run --rm to automatically delete it when it exits.
Run and Remove:

docker run --rm image_name 

docker run -d -t --name container1 busybox

docker attach container1 
Control-C
docker ps

Remove the container after stop
docker run --rm -it --name container1 busybox


Remove all exited containers

You can locate containers using docker ps -a and filter them by their status: created, restarting, running, paused, or exited. To review the list of exited containers, use the -f flag to filter based on status. When you've verified you want to remove those containers, using -q to pass the IDs to the docker rm command.
 

docker ps -a -f status=exited

Remove all exited containers
docker rm $(docker ps -a -f status=exited -q)

Remove containers using more than one filter

Docker filters can be combined by repeating the filter flag with an additional value. This results in a list of containers that meet either condition. For example, if you want to delete all containers marked as either Created (a state which can result when you run a container with an invalid command) or Exited, you can use two filters:

List:

docker ps -a -f status=exited -f status=created
Remove:

docker rm $(docker ps -a -f status=exited -f status=created -q)

Remove containers according to a pattern

You can find all the containers that match a pattern using a combination of docker ps and grep. When you're satisfied that you have the list you want to delete, you can use awk and xargs to supply the ID to docker rmi. Note that these utilities are not supplied by Docker and not necessarily available on all systems:

List:

docker ps -a |  grep "pattern”

Remove:

docker ps -a | grep "pattern" | awk '{print $3}' | xargs docker rmi

Stop and remove all containers

You can review the containers on your system with docker ps. Adding the -a flag will show all containers. When you're sure you want to delete them, you can add the -q flag to supply the IDs to the docker stop and docker rm commands:

List:

docker ps -a

Remove All containers

docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)


Removing Volumes
Remove one or more specific volumes - Docker 1.9 and later

Use the docker volume ls command to locate the volume name or names you wish to delete. Then you can remove one or more volumes with the docker volume rm command:

List:

docker volume ls
Remove:

docker volume rm volume_name volume_name

Remove dangling volumes - Docker 1.9 and later

Since the point of volumes is to exist independent from containers, when a container is removed, a volume is not automatically removed at the same time. When a volume exists and is no longer connected to any containers, however, it's called a dangling volume. To locate them to confirm you want to remove them, you can use the docker volume ls command with a filter to limit the results to dangling volumes. When you're satisfied with the list, you can add a -q flag to provide the volume name to docker volume rm:

List:

docker volume ls -f dangling=true
Remove:

docker volume rm $(docker volume ls -f dangling=true -q)

Remove a container and its volume

If you created an unnamed volume, it can be deleted at the same time as the container with the -v flag. Note that this only works with unnamed volumes. When the container is successfully removed, its ID is displayed. Note that no reference is made to the removal of the volume. If it is unnamed, it is silently removed from the system. If it is named, it silently stays present.

Remove:

docker rm -v container_name

*******************************

 The docker load command loads a tarred repository from a file or the standard input stream. 
 It restores both images and tags.


docker load < busybox.tar.gz
docker load --input fedora.tar

 

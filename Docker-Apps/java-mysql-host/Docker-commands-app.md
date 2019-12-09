 
docker with stateful conatiners
docker logging and tracing
docker with spring boot microservice
On windows check without docker machine run an image(stop the default machine)
Isolate the docker container logs

Docker installation
Linux machine : Direct installation
Windows 10 with Docker for Windows : Direct installation
windows 7 with Docker toolBox : With Oracle VM Box


Docker for Windows PC

An integrated, easy-to-deploy development environment for building, debugging and testing Docker apps on a Windows PC. Docker for Windows is a native Windows app deeply integrated with Hyper-V virtualization, networking and file system, making it the fastest and most reliable Docker environment for Windows.

Docker for Windows PC is available for free for Download Now from Docker Store, It requires Microsoft Windows 10 Professional or Enterprise 64-bit edition.For earluer version of Windows use Docker Toolbox which supports Oracle VM with docker(by creating linux VM on windows)

When people say “Docker” they typically mean Docker Engine, the client-server application made up of the Docker daemon, a REST API that specifies interfaces for interacting with the daemon, and a command line interface (CLI) client that talks to the daemon (through the REST API wrapper). Docker Engine accepts docker commands from the CLI, such as docker run <image>, docker ps to list running containers, docker images to list images, and so on.

Docker Machine is a tool for provisioning and managing your Dockerized hosts (hosts with Docker Engine on them). Typically, you install Docker Machine on your local system. Docker Machine has its own command line client docker-machine and the Docker Engine client, docker. You can use Machine to install Docker Engine on one or more virtual systems. These virtual systems can be local (as when you use Machine to install and run Docker Engine in VirtualBox on Mac or Windows) or remote (as when you use Machine to provision Dockerized hosts on cloud providers). The Dockerized hosts themselves can be thought of, and are sometimes referred to as, managed “machines”.



  Check wheteher docker is ruinning
  docker info

 OR to display the doscker running contaienrs
 docker ps

To display active docker images:
docker ps -a

 To run an image in intercative(attached) mode
 docker run -it ubuntu bash


  To Run the app-image in detacheed mode
  docker run -d test-app:v1

  Change to the Docker direcory is current user path

  cd Docker

  docker build -t user-service-app .

  docker build -t user-service-app:v1 .

  To Run the user-service-app image in detacheed mode
  docker run -d user-service-app:v1 



  Load an image from a tar archive or STDIN

 From any other path
 docker build -f /home/administrator/Desktop/Docker-Applications/Docker-apps-deployed/py-app/Dockerfile -t test-app:v1 ."


  The docker load command loads a tarred repository from a file or the standard input stream. 
 It restores both images and tags.


docker load < busybox.tar.gz
docker load --input fedora.tar

  docker images
  

  To Run the app-image in detacheed mode
  docker run -d test-app:v1 
 
  Run with host name
  docker run -d -h py-host test-app:v1

  Run with container and host name assigned
 docker run -d --name my_container -h py-host test-app:v1 

To make this app available outside the docker container

   Run the test-app with host port attached to docker container
To run the app by mapping the current machines port 4000 to the containers published port 80 using -p:
  
 Log in to the Docker public registry on your local machine.

  docker login

  Publish the image on docker hub in the format
  docker tag image username/repository:tag

 

 docker tag user-service-app:v1 pbadhe34/my-apps:user-app


 docker tag test-app pbadhe34/my-apps:app1
 
  docker images
  docker images ls

  To Publish the image to docker hub
  Upload your tagged image to the repository:

  docker push pbadhe34/my-apps:user-app

Pull and run the image from the remote repository
From now on, you can use docker run and run your app on any machine with this command in the format
docker run -p 4000:8090 username/repository:tag

docker run -d -p 3000:8090 pbadhe34/my-apps:app1



Docker-machine ip
No default mc exists on linux.

docker-machine create default

Docker-machine ip : ip address of local host

Map to Docker host machine physical address with port on Linux

On Windows it maps to docker machine addresss(The VM address)

 docker run -d -p 4000:8090 --name my_container -h py-host test-app:v1

On linux host
curl http://<host-address>:4000
curl http://localhost:4000
curl http://127.0.0.1:4000

On windows(The docker machine(VM) address and NOT the physical address)
curl http://192.168.99.100:4000

 Map to docker machine ip address

docker run -d -p 192.168.99.100:3500:8090 --name my_container -h py-host test-app:v1


Map to local host address on Linux
docker run -d -p 127.0.0.1:3500:8090 --name my_container -h py-host test-app:v1

To Run the app-image in detacheed mode on docker machine on linux

  docker-machine create --driver virtualbox mc1

 docker-machine ip mc1 -->192.168.99.100 

 docker-machine ssh mc1 "docker run -d -p 3000:8090 pbadhe34/my-apps:app1"

  docker-machine ssh mc1 "docker container ls"
 docker-machine ssh mc1
  -->docker attach <containerid>
  -->docker stop

  http://192.168.99.100:3000


  docker-machine ssh mc1 "docker run -d -p 3000:8090 test-app:v1"   //image not available locally

  To Build on this machine mc1, copy the directoty py-app to mc1 machine from the parent of py-app
   docker-machine ssh mc1 pwd  : /home/docker

  copy file user.txt from current direectory
  docker-machine scp mc1:/home/docker/user.txt .

  copy the py-app dir to mc1 machine
  docker-machine scp -r -d py-app/ mc1:/home/docker/py-app/

  r - ecudsive copy
  d - delta(diff) copy; to reduce data to be sent

  docker-machine ssh mc1 "docker build -t test-app:v1 ."  --> /home/docker/Dockerfile: no such file or directory

  docker-machine ssh mc1
  -->docker build -t test-app:v1 .  
  -->docker run -d -p 3200:8090 test-app:v1
  -->docker  container ls
   -->docker logs <contain er id>
  -->docker stop..
   -->docker rm ..
  -->exit

http://192.168.99.100:3200

 Run From the py-app directory
  docker-machine ssh mc1 "docker build -f /home/administrator/Desktop/Docker-Applications/Docker-apps-deployed/py-app/Dockerfile -t test-app:v1 ."

curl http://localhost:3500/  OR curl http://127.0.0.1:3500/

binding to the docker host's 127.0.0.1. Since the docker host is in a VM on Windows, that's different from the external 127.0.0.1 on the system.

docker run -d --rm  -p 3000:8090 --name my_container -v $(pwd):/user/prakash/py-app test-app:v1 will bind to 192.168.99.100:3000

curl http://192.168.99.100:3000/


docker run -d -p 3200:8090 --name my_container -h py-host pbadhe34/my-apps:app1

curl http://192.168.99.100:3200/

docker ps

curl http://127.0.0.1:3500

Mapping to physical IP address is possibkle with Linux Bare metal without VM instance

docker run -d -p 192.168.0.100:3200:8090 --name my_container -h py-host test-app:v1

curl http://192.168.0.100:3200


Map to the machine addreess
docker run -d -p 192.168.99.100:3200:8090 --name my_container -h py-host test-app:v1

curl http://192.168.99.100:3200




docker exec -it <container name> <command> to execute whatever command you specify in the container.

docker attach will let you connect to your Docker container, but this isn't really the same thing as ssh. If your container is running a webserver, for example, docker attach will probably connect you to the stdout of the web server process. It won't necessarily give you a shell.


docker attach my_container : dipsly the container log on stdOut terminal.

docker exec -it my_container /bin/bash
cat /etc/hosts
pwd
history

start a shell in the container;

docker exec -it my_container sh
 hostname -I 

docker exec -it  my_container bash

docker exec -it  $(docker ps -q) bash: worlks on last conatiner created

Export the environmental variables from the running container
docker exec -i -t $(docker ps -l -q) env | grep ADDR
 

docker exec -i -t $(docker ps -l -q) ip a

Add -q to automatically parse and return the last CID created.
docker inspect --format '{{ .NetworkSettings.IPAddress }}' $(docker ps -q)
172.17.0.1
 

docker attach my-container

Attach to STDIN/STDOUT/STDERR (-a)
The -a flag tells docker run to bind to the containers STDIN, STDOUT or STDERR. This makes it possible to manipulate the output and input as needed.

echo "test" | docker run -i -a stdin busybox cat -

This pipes data into a container and prints the containers ID by attaching only to the containers STDIN.

docker run -a stderr busybox echo test

This isnt going to print anything unless theres an error because weve only attached to the STDERR of the container. The containers logs still store whats been written to STDERR and STDOUT.

cat somefile | docker run -i -a stdin mybuilder dobuild

This is how piping a file into a container could be done for a build. The containers ID will be printed after the build is done and the build logs could be retrieved using docker logs. This is useful if you need to pipe a file or something else into a container and retrieve the containers ID once the container has finished running.



To get the redis working with HitCounter

 docker run -d -p 2000:6379 --name redis -h redis redis and link with test-app

 docker network inspect bridge
docker network inspect host

 docker top CONTAINER-Name [ps OPTIONS]: To Display the running processes of a container

  docker top	my_container

  docker top	my_container <process-pid>


  docker port my_container

  docker-machine ip 

  curl http://192.168.99.100:4000


  docker ps

 docker container ls  

 docker container ls -a

  The app is running on :http://192.168.99.100:4000  
  
Too see the docker container choosen port. 
Access is then possible via localhost:port.

docker port <container id/name>

  docker-machine ip 

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

docker network inspect host

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

Add entries to container hosts file (add-host)
You can add other hosts into a containers /etc/hosts file by using one or more --add-host flags. This example adds a static address for a host named user-host:

docker run -d --add-host=user-host:192.168.0.100 --rm -it pbadhe34/my-apps:app1

  


The Python is serving your app at http://0.0.0.0:80. But that message is coming from inside the container, which doesnt know you mapped port 80 of that container to 4000, making the correct URL http://localhost:4000.

   To check the list of containers running

   docker container ls
   
   Container ID with docker image is displayed

   To stop the cotainer

   docker stop <container-id/name>

  docker pause <container-id/name>

  docker start <container-id/name>


  docker rm <container-id/name>

 
  Log in to the Docker public registry on your local machine.

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

 If the image isnt available locally on the machine, Docker will pull it from the repository.

To get the redis working with HitCounter

 docker run -d --name redis -h redis redis

 If you dont specify the :tag portion of these commands, the tag of :latest will be assumed, both when you build and when you run images. Docker will use the last version of the image that ran without a tag specified (not necessarily the most recent image).

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

If you know when youre creating a container that you wont want to keep it around once youre done, you can run docker run --rm to automatically delete it when it exits.
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

docker ps -a |  grep "pattern

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


 

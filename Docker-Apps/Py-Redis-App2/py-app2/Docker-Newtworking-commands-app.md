 

  Check wheteher docker is ruinning
  docker info

 docker version

  

  Change to the py-app direcory is current user path

  cd py-app2

  docker build -t test-app .

  docker build -t test-app:v1 .



docker images


docker images ls
Format the image output
docker images --format "{{.ID}}: {{.Repository}}"

docker images test-app --format "{{.ID}}: {{.Repository}}"

docker images --format "table {{.ID}}\t{{.Repository}}\t{{.Tag}}"
  

///***************************************

 To Run the app-image in detacheed mode
  docker run -d test-app:v1

  After the The inspect command

 docker inspect <containerID>

  Gateway": "172.17.0.1",  (Same as docker0 addresss in ifconfig : NOT the physiacl IP address)
  "IPAddress": "172.17.0.2",(The container ip address)
  
 You can PING both of the above addresses from local machine.
 Test by sending request to container

 curl http://172.17.0.2:8090

  Also in the browser

 http://172.17.0.2:8090

 But both of Above will not work from another physiacl host 
 For that map it to physiacl host

 With Physical host ip addresss

  curl http://192.168.0.105:8090  : Connection Refused

Map to host ip


 docker run -d test-app:v1


 Run with host port mapping to make ita ccaessible outside host


docker run -d -p 127.0.0.1:8090:8090 test-app:v1


 
  docker inspect

  Gateway": "172.17.0.1",
 "IPAddress": "172.17.0.3",

  "Ports": {
                "8090/tcp": [
                    {
                        "HostIp": "127.0.0.1",
                        "HostPort": "8090"
                    }
                ]

 Accessible through : http://localhost:8090/  or http://127.0.0.1:8090/
  But not still through :http://192.168.0.105:8090/ Where 192.168.0.105 is the physical ip adress of host


 docker run -d -p 8090:8090 test-app:v1

 OR

 docker run -d -p 192.168.0.105:8090:8090 test-app:v1

docker run -d -p 192.168.0.105:8070:8090 test-app:v1

To display active/running docker containers:
docker ps -a


To run an image in intercative(attached) mode
 docker run -it ubuntu bash
  
 
  Run with host name
  docker run -d -h py-host test-app:v1

  Run with container and host name assigned
 docker run -d --name my_container -h py-host test-app 

docker run -d -p 8090:8090 --name my_container -h py-host test-app 


To make this app available outside the docker container

Run the test-app with host port attached to docker container
To run the app by mapping the current machines port 4000 to the containers published port 80 using -p:
  
Map to Docker machien address and port

 docker run -d -p 4000:8090 --name my_container -h py-host test-app:v1

curl http://192.168.99.100:4000

 
Map to local host address
docker run -d -p 127.0.0.1:3500:8090 --name my_container -h py-host test-app:v1

 docker run -d --rm -it -p 3000:8090 --name my_container -v $(pwd):/user/prakash/py-app test-app:v1    :will bind to 192.168.99.100:3000 and get removed when NO usage.


curl http://192.168.99.100:3000/

 Run with host network (Default is bridge)

docker run -d --network host test-app:v1  : (No Container IP address and the docker container is mapped to host address)

 Run without network

docker run -d --net none test-app:v1  (No Container IP address)

 Run with default (bridge) network

docker run -d test-app:v1  OR

docker run -d --net bridge test-app:v1

For bridge networked containers created, a new network connection apperas in output of 'ifconfig'
This manages the container networking.


with dynamic port mapping

docker run --name app-container -p 8090 test-app:v1

Static port mapping
docker run -it -d -p 4000:8090 --link redis-container:redis --name my-container -h my-host test-app


docker run -d -p 3200:8090 --name my_container -h py-host pbadhe34/my-apps:app1

curl http://192.168.99.100:3200/

docker ps

curl http://127.0.0.1:3500

Mapping to physical IP address is possibkle with Linux Bare metal without VM instance

docker run -d -p 192.168.0.100:3200:8090 --name my_container -h py-host test-app:v1

curl http://192.168.0.100:3200

 Mapping to Docker container adress


Map to the machine addreess
docker run -d -p 192.168.99.100:3200:8090 --name my_container -h py-host test-app:v1

curl http://192.168.99.100:3200

docker run -d -p 127.0.0.1:3100:8090 --name my_container -h py-host test-app:v1

With dynamic port mapping

docker run --name app-container -p 8090 test-app:v1

To read the dynamic port assignned from  host to the container


docker inspect --format='{{(index (index .NetworkSettings.Ports "80/tcp") 0).HostPort}}' app-container
///******************


Enable forwarding from Docker containers to the outside world

By default, traffic from containers connected to the default bridge network is not forwarded to the outside world. 
To enable forwarding, you need to change two settings. 
These are not Docker commands and they affect the Docker host’s kernel.

    Configure the Linux kernel to allow IP forwarding.

    $ sysctl net.ipv4.conf.all.forwarding=1

    Change the policy for the iptables FORWARD policy from DROP to ACCEPT.

    $ sudo iptables -P FORWARD ACCEPT

These settings do not persist across a reboot, so you may need to add them to a start-up script.


//////////////////********
 Run with different Network mode

docker run -d --name app-container  nginx  : default network is is bridge
docker run -d --name app-container  --network bridge nginx 

docker run -d --name app-container --network host nginx

docker run -d --name app-container  --network none nginx

docker run -d --name app-container --network host nginx

For user defined networks
docker run -d --name app-container  --ip 192.168.99.100 --network bridge nginx



///////////////**********************

*********************************
Docker compose YML file for Docker Custom Network configuration




***************************************************
Docker networking
A bridge network is a Link Layer device which forwards traffic between network segments.
A bridge can be a hardware device or a software device running within a host machine’s kernel.

In  Docker, a bridge network uses a software bridge which allows containers connected to the same bridge network to communicate, 
while providing isolation from containers which are not connected to that bridge network. 
The Docker bridge driver automatically installs rules in the host machine so that containers on different bridge 
networks cannot communicate directly with each other.

Bridge networks apply to containers running on the same Docker daemon host.
When start Docker, a default bridge network (also called bridge) is created automatically,
 and newly-started containers connect to it unless otherwise specified. 
You can also create user-defined custom bridge networks. 
User-defined bridge networks are superior to the default bridge network.


For communication among containers running on different Docker daemon hosts, 
you can either manage routing at the OS level, or you can use an 'overlay' network.
This overlay network also gets created in Docker swarm mode which manages communication across docker daemon hosts.

Containers connected to the default bridge network can communicate, but only by IP address, unless they are linked using the 
legacy --link flag.
Containers connected to the same user-defined bridge network automatically expose all ports to each other,
 and no ports to the outside world. 
This allows containerized applications to communicate with each other easily,
 without accidentally opening access to the outside world.



The 'docker0' manages the vethXXX interfaces on host machine.

For bridge networks when a container gets created, a new network connection apperas in output of 'ifconfig' by names 'vethxxx'
This manages the container networking.
When a container is launched it creates a peer interfaces, 
one inside the container named “eth0” and other on the host machine named vethxxxxxxx where “xxxxxxx” 
is a unique string.

Single container creates single interface on host machine, 2 containers create two interface on hosts and so on…

The 'veth*' interfaces are the interfaces which got created on host machine when we run container.

-> ip route show

->ip addr show

  -> ip address show dev docker0

-->bridge showmacs docker0

->bridge showstp docker0

 -> bridge link
  Shows the vethcxxx bridge linik connections created for container running with bridge networks
  
36: veth6c01682 state UP @(null): <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 master docker0 state forwarding priority 32 cost 2 
38: vetha829645 state UP @(null): <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 master docker0 state forwarding priority 32 cost 2 


The brctl command has to be installed with:
sudo apt-get install bridge-utils

The veth* could be listed with the following command:
sudo brctl show

To find the relation btween container addresss and veth*
by matching a container interface’s 'iflink' value with a host veth interface’s ifindex value.

On the container, run :
cat /sys/class/net/eth0/iflink
-->6

And on the host, find a veth with an ifindex value matching the iflink value of your container’s interface :
cat /sys/class/net/veth515e91c/ifindex
 OR
grep -l 6 /sys/class/net/veth*/ifindex 


The 'iflink' - Returns whether or not the system has a network link.,0 for no, 1 for yes.

To get the relation between the network interface and container use iflink from a container and ifindex on the host machine.

Get iflink output from a container:

docker exec -it 64191f85f875 /bin/bash
->cat /sys/class/net/eth0/iflink
 ->38
->Exit

 

$ docker exec <containerID> cat /sys/class/net/eth0/iflink  --> 38

->docker exec 64191f85f875 cat /sys/class/net/eth0/iflink

->38
This number 38 is lnmked to 'vetha829645' bridge interface.

38: vetha829645
Then find this 'ifindex' among interfaces on the host machine:

$ grep -l 38 /sys/class/net/veth*/ifindex 
The output : /sys/class/net/vetha829645/ifindex.

///////////*******************************************

Configure the Default Bridge network

Configure the default bridge network

To configure the default bridge network, you specify options in daemon.json. Here is an example daemon.json with several options specified. Only specify the settings you need to customize.

{
  "bip": "192.168.1.5/24",
  "fixed-cidr": "192.168.1.5/25",
  "fixed-cidr-v6": "2001:db8::/64",
  "mtu": 1500,
  "default-gateway": "10.20.1.1",
  "default-gateway-v6": "2001:db8:abcd::89",
  "dns": ["10.20.1.2","10.20.1.3"]
}

You need to restrt the docker for the changes to take effect.

///**************************************
Custom Networks

Containers connected to the same user-defined bridge network automatically expose all ports to each other,
 and no ports to the outside world. 
This allows containerized applications to communicate with each other easily, without accidentally opening access to the outside world.

Containers on the default bridge network can only access each other by IP addresses, unless you use the --link option, 
which is considered legacy. 
On a user-defined bridge network, containers can resolve each other by name or alias.

To remove a container from the default bridge network, you need to stop the container and recreate it with different network options.
In user-defined networks, a container’s lifetime, you can connect or disconnect it from user-defined networks on the fly.
In docker-compose yml files you specify anuser defined networks.

If your containers use the default bridge network, you can configure it, but all the containers use the same settings,
 such as MTU and iptables rules. 
In addition, configuring the default bridge network happens outside of Docker itself, and requires a restart of Docker.
User-defined bridge networks are created and configured using docker network create. If different groups of applications 
have different network requirements, you can configure each user-defined bridge separately, as you create it.(as in docker compose examples)


Example :  an application with a web front-end and a database back-end. 
The outside world needs access to the web front-end (perhaps on port 80), but only the back-end itself needs access 
to the database host and port. Using a user-defined bridge, only the web port needs to be opened, 
and the database application doesn’t need any ports open, since the web front-end can reach it over the user-defined bridge.

If you run the same application stack on the default bridge network,all ports are open for containers on same bridge network.
Containers connected to the same user-defined bridge network effectively expose all ports to each other.


This means the Docker host needs to block access to the database port by other means.

For a port to be accessible to containers or non-Docker hosts on different networks,
 that port must be published using the -p or --publish flag.

 Sharing
Linked containers on the default bridge network share environment variables.

Originally, the only way to share environment variables between two containers was to link them using the --link flag. This type of variable sharing is not possible with user-defined networks. 
However, there are superior ways to share environment variables. A few ideas:

    Multiple containers can mount a file or directory containing the shared information, using a Docker volume.

    Multiple containers can be started together using docker-compose and the compose file can define the shared variables.

    You can use swarm services instead of standalone containers, and take advantage of shared secrets and configs



////**********************

Use the docker network create command to create a user-defined bridge network.

$ docker network create my-net
You can specify the subnet, the IP address range, the gateway, and other options. See the docker network create reference or the output of docker network create --help for details.

Use the docker network rm command to remove a user-defined bridge network. If containers are currently connected to the network, disconnect them first.

$ docker network rm my-net

When you create or remove a user-defined bridge or connect or disconnect a container from a user-defined bridge, Docker uses tools specific to the operating system to manage the underlying network infrastructure (such as adding or removing bridge devices or configuring iptables rules on Linux). These details should be considered implementation details. Let Docker manage your user-defined networks for you.

Connect a container to a user-defined bridge

docker create --name my-nginx \
  --network my-net \
  --publish 8080:80 \
  nginx:latest

To connect a running container to an existing user-defined bridge, use the docker network connect command. The following command connects an already-running my-nginx container to an already-existing my-net network:

$ docker network connect my-net my-nginx


To disconnect a running container from a user-defined bridge, use the docker network disconnect command. The following command disconnects the my-nginx container from the my-net network.

$ docker network disconnect my-net my-nginx

DNS services for Containers

By default, a container inherits the DNS settings of the Docker daemon,
 including the /etc/hosts and /etc/resolv.conf.

You can override these settings on a per-container basis
Flag 	Description
--dns 	The IP address of a DNS server. To specify multiple DNS servers, use multiple --dns flags. If the container cannot reach any of the IP addresses you specify, Google’s public DNS server 8.8.8.8 is added, so that your container can resolve internet domains.
--dns-search 	A DNS search domain to search non-fully-qualified hostnames. To specify multiple DNS search prefixes, use multiple --dns-search flags.
--dns-opt 	A key-value pair representing a DNS option and its value. See your operating system’s documentation for resolv.conf for valid options.
--hostname 	The hostname a container uses for itself. Defaults to the container’s ID if not specified.


*************************************************************************************

 To stop and remove all the conrainers
docker stop $(docker ps -aq)

docker rm $(docker ps -aq)

 To clean

 docker system prune


To remove all dangling images and non-running containers and other objects

 docker system prune



 ***********************************************

Linking the containers


To get the redis container running  

docker run -d --name redis-container -h redis-host redis

Link the redis container to py-app container whle starting

docker run -it -d -p 4000:8090 --link redis-container:redis --name my-container -h my-host test-app

curl http://172.17.0.4:8090

 The value provided to the link flag is sourcecontainername:containeraliasname. The value redis-container  in the sourcecontainername since that was the name that was given to our first container that launched earlier. 
The containeraliasname has been selected as redis and it could be any name of choice.

docker inspect  app-container

 **********************************************
Docker publish image to Docker Hub
To  Publish the image on docker hub in the format : tag it
  docker tag image username/repository:tag

 docker tag test-app pbadhe34/my-apps:app3
 
  Log in to the Docker public registry on your local machine.

  docker login

 
  docker images
  docker images ls

  To Publish the image to docker hub
  Upload your tagged image to the repository:

  docker push pbadhe34/my-apps:app3

Remove the local image built earlier
docker rmi test-app

Pull and run the image from the remote repository
From now on, you can use docker run and run your app on any machine with this command in the format
docker run -p 4000:8090 username/repository:tag

docker run -d -p 3000:8090 pbadhe34/my-apps:app3

docker run -d -p 3000:8090 --network host pbadhe34/my-apps:app3 



 If the image isnt available locally on the machine, Docker will pull it from the repository.




////////////*****************************

 Linkiing the containers

To get the redis working with HitCounter

docker run -d --name redis-app -h redis-host redis 

and link with test-app container app

docker run -d -p 4000:8090 -it --link redis-app:redis --name app  -h app-host pbadhe34/my-apps:app3


Check in the browser

http://192.168.99.100:4000/

Stop the app container and redstart again..
 and check the hit counter

*************************************

Assign volume to redis-container

Assign Volume to Redis container  and link to app-container

Create directory redis-volume on home/dir

docker run -d --name redis-container -h redis-host -v /redis-volume:/data redis 



Adding a shared volume from host mc os
Add shared volume from Host OS to the container
Mounting a Host Directory as a Data volume
Now that we have seen how to mount a volume in the container, the next step is to look at the same process of mounting a volume but this time we will mount an existing host folder in the Docker container. This is an interesting concept and is very useful if you are looking to do some development where you regularly modify a file in a folder outside and expect the container to take note or even sharing the volumes across different containers.

To mount a host volume while launching a Docker container, we have to use the following format for volume -v :
-v HostFolder:ContainerVolumeName

 

docker volume inspect <volume-name>

Assign Volume to Redis container  and link to app-container

docker run -d --name redis-app -h redis-host -v /d/data/app-volume:/data redis 

With link to redis container

docker run -d -p 4000:8090 -it --link redis-app:redis --name app  -h app-host pbadhe34/my-apps:app1


*********************

Stop and rermove redis-container

 docker stop redis-container

 docker rm redis-container

 Run it gain and see staored data with Volume



Add avolumr tyop Redis container if neeedd
docker run -d  --name redis-container -h redis-host -v /c/Users/redis-data:/data redis 


docker inspect -f '{{ .Mounts }}' app

docker volume ls
docker vlume inspect <volumename>
docker inspect -f '{{ (index .Mounts 0).Source }}' containerid

 docker inspect -f '{{ json .Mounts }}' containerid | python -m json.tool 

docker inspect -f '{{ json .Mounts }}' containerid | jq 

***********************************************



/////////////**********************Docker exec/ attach/********

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



docker network inspect bridge
docker network inspect host

 docker top CONTAINER-Name [ps OPTIONS]: To Display the running processes of a container

  docker top	my_container

  docker top	my_container <process-pid>


  docker port my_container

  docker-machine ip 

 Tets it with curl

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

************************************

  Docker Insopect Containers

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


Docker linking the conatiners

To get the redis working with HitCounter

 docker run -d --name redis -h redis redis

 If you dont specify the :tag portion of these commands, the tag of :latest will be assumed, both when you build and when you run images. Docker will use the last version of the image that ran without a tag specified (not necessarily the most recent image).

List images by name and tag
docker images test-app

List the full length image IDs
docker images --no-trunc

List all exited containers
docker ps -aq -f status=exited

Remove stopped containers
docker ps -aq --no-trunc | xargs docker rm



*********************************************
Docker remove containers and images

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

*****************************
 Load an image from a tar archive or STDIN


  The docker load command loads a tarred repository from a file or the standard input stream. 
 It restores both images and tags.


docker load < busybox.tar.gz
docker load --input fedora.tar

********************************


 

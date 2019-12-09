To share the data and files Volumes are defined
There are 2 ways in which you can manage data in Docker:
1.Data volumes
2. Data volume containers

Data Volume is a specially designed directory in the container.
1.It is initialized when the container is created. By default, it is not deleted when the container is stopped. It is not even garbage collected when there is no container referencing the volume.
2. The data volumes are independently updated.
3. Data volumes can be shared across containers too. They could be mounted in read-only mode too.


To add a volume for our container. 
docker run -it -v /data --name container1 busybox

ls

navigate to data directory (/data) and then create a file in it.
cd data
/data # touch file1.txt
/data # ls
file1.txt
ls


exit

docker ps -a


docker container ls -a

docker attach container1
ls
cd data
ls
 

(In detached mode
docker run -d -v /data --name container1 busybox)



docker ps -a , The docker(container1) currently in the exited state as shown below:


docker inspect container1
..
..
"Mounts": [
    {
        "Type": "volume",
        "Name": "1f4af03a6704afb48733290260b291d4f983a322282d88aca2890f5
9",
        "Source": "/mnt/sda1/var/lib/docker/volumes/1f4af03a6704afb48733
91d4f983a322282d88aca2890f5a3fe11da9/_data",
        "Destination": "/data",
        "Driver": "local",
        "Mode": "",
        "RW": true,
        "Propagation": ""
    }
],..

docker stop container1

docker rm container1

docker volume ls
docker volume rm <volumeid>


docker rm --help

To remove the volume with container
docker -v rm container1

Mounting a Host Directory as a Data volume
Now that we have seen how to mount a volume in the container, the next step is to look at the same process of mounting a volume but this time we will mount an existing host folder in the Docker container. This is an interesting concept and is very useful if you are looking to do some development where you regularly modify a file in a folder outside and expect the container to take note or even sharing the volumes across different containers.

To mount a host volume while launching a Docker container, we have to use the following format for volume -v :
-v HostFolder:ContainerVolumeName

docker run -it --name container1 -v /c/Users:/Volume-Data
busybox
ls
cd c:/users/-->newDir Volume-Data
touch file1.txt

 
Volume-Data-->Current emopy folder and 

Touch
Volume-Data-->

mkdir app2
docker run -it -v /app2:/myapp --name container busybox

The app2 dir is mapped and mounteed as myapp  inside the 
container1 

we have mapped the host folder /c/Users to a volume /datavol that will be  mounted inside our container (container1).
Now, if we do a ls , we can see that the /datavol has been mounted. Do a cd into that folder and a ls, and you should be able to see the folder contents of C:\Users on your machine.

The Container with ReadOnly Volume

Specify the :ro as shown below to make the volume readonly.

docker run -it -v /ubuntu2:/ubuntu2:ro --name container busybox

 
/ # cd ubuntu2/
/ubuntu2 # touch file
touch: file: Read-only file system
/ubuntu2 # exit


Set environment variables (-e, –env, –env-file)
docker run -e MYVAR1 --env MYVAR2=foo --env-file ./env.list ubuntu bash

define the variable and its value when running the container:

docker run --env VAR1=value1 --env VAR2=value2 ubuntu env | grep VAR

Use variables that you’ve exported to the local environment:

export VAR1=value1
export VAR2=value2

docker run --env VAR1 --env VAR2 ubuntu env | grep VAR
VAR1=value1
VAR2=value2


Mount volumes from container (–volumes-from)
docker run --volumes-from 777f7dc92da7 --volumes-from ba8c0c54f0f2:ro -i -t ubuntu pwd

The --volumes-from flag mounts all the defined volumes from the referenced containers. Containers can be specified by repetitions of the --volumes-from argument. The container ID may be optionally suffixed with :ro or :rw to mount the volumes in read-only or read-write mode, respectively. By default, the volumes are mounted in the same mode (read write or read only) as the reference containers.

add -t to the docker run command, which will attach a pseudo-TTY. Then you can type Control-C to detach from the container without terminating it.

docker run -it -v /data --name container1 busybox
The i for ineractive and t for psuedo TTY

Once you have attached to a Docker Container via a CMD console typing exit at the console detatches from the container and Stops it. 
To detatch from the container without stopping it press CTRL+P followed by CTRL+Q. 



Data volume containers
The Data volume container are useful to share data between containers or you want to use the data from non-persistent containers.  
You first create a Data volume container
Create another container and mount the volume from the container created in Step 1.
 

Create a container (container1) and mount a volume inside of that:
docker run -it -v /data --name container1 busybox


into the /data volume and create two dummy files in it as shown below:
/ # cd data
/data # ls
/data # touch file1.txt
/data # touch file2.txt
/data #

Press ctrl + C and NOT the  exit command

docker exec container1 ls /data

docker ps -a

Launch another container (container2) but it will mount the data volume from container1 as given below:

docker run -it --volumes-from container1 --name container2 busybox

ls 
 
/ # cd data
/data # ls
file1.txt file2.txt
/data #


press Ctrl-P-Q to come back to the docker prompt without exiting the container.This turns interactive mode to daemon mode
Now, if we do a docker ps, we should see our running container:

Mounting dirs and files in docker compose files

 volumes:
      - /docker/myapp/upload:/var/www/html/upload
      - /src/docker/myapp/config.php:/var/html/config.php

File as shared volume

docker run -it -v /test/user.txt --name container1 busybox

Mounting File as shared volume from the host
docker run -it -v /app2/test.txt:/myapp/flag.txt --name container busybox

cd myapp
vi 
exit

docker exec container ls /myapp



To quit the Vi editor in terminal 
If you are currently in insert or append mode, press Esc.
Press : (colon). The cursor should reappear at the lower left corner of the screen beside a colon prompt.
Enter the following:
 q!


Use of mount and -v

docker run -d \
  -it \
  --name devtest \
  --mount source=myvol2,target=/app \
  nginx:latest

$ docker run -d \
  -it \
  --name devtest \
  -v myvol2:/app \
  nginx:latest

Start a service with volumes

The docker service create command does not support the -v or --volume flag. When mounting a volume into a service’s containers, you must use the --mount flag.

docker service create -d \
  --replicas=4 \
  --name dev-service \
  --mount source=myvol2,target=/app \
  nginx:latest


opulate a volume using a container
If you start a container which creates a new volume, as above, and the container has files or directories in the directory to be mounted (such as /app/ above), the directory’s contents will be copied into the volume. The container will then mount and use the volume, and other containers which use the volume will also have access to the pre-populated content.

Start an nginx container and populates the new volume nginx-vol with the contents of the container’s /usr/share/nginx/html directory, which is where Nginx stores its default HTML content.

The --mount and -v examples have the same end result.

$ docker run -d \
  -it \
  --name=nginxtest \
  -v nginx-vol:/usr/share/nginx/html \
  nginx:latest

docker run -d \
  -it \
  --name=nginxtest \
  --mount source=nginx-vol,destination=/usr/share/nginx/html \
  nginx:latest

Use a read-only volume

docker run -d \
  -it \
  --name=nginxtest \
  -v nginx-vol:/usr/share/nginx/html:ro \
  nginx:latest

docker run -d \
  -it \
  --name=nginxtest \
  --mount source=nginx-vol,destination=/usr/share/nginx/html,readonly \
  nginx:latest

Use a volume driver
When you create a volume using docker volume create, or when you start a container which uses a not-yet-created volume, you can specify a volume driver. The following examples use the vieux/sshfs volume driver, first when creating a standalone volume, and then when starting a container which will create a new volume.
Initial set-up
This example assumes that you have two nodes, the first of which is a Docker host and can connect to the second using SSH.

On the Docker host, install the vieux/sshfs plugin:

$ docker plugin install --grant-all-permissions vieux/sshfs

Create a volume using a volume driver
This example specifies a SSH password, but if the two hosts have shared keys configured, you can omit the password. Each volume driver may have zero or more configurable options, each of which is specified using an -o flag.

$ docker volume create --driver vieux/sshfs \
  -o sshcmd=test@node2:/home/test \
  -o password=testpassword \
  sshvolume

Start a container which creates a volume using a volume driver
This example specifies a SSH password, but if the two hosts have shared keys configured, you can omit the password. Each volume driver may have zero or more configurable options. If the volume driver requires you to pass options, you must use the --mount flag to mount the volume, rather than -v.

$ docker run -d \
  -it \
  --name sshfs-container \
  --volume-driver vieux/sshfs \
  --mount src=sshvolume,target=/app,volume-opt=sshcmd=test@node2:/home/test,volume-opt=password=testpassword \
  nginx:latest




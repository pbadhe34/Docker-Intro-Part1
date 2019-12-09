
To start and stop the docker daemon

systemctl enable docker
systemctl start docker
sudo systemctl stop docker

docker history <image>



To view the contents of Docker folder

sudo ls /var/lib/docker/


OPen the restricted folders

1. sudo apt install gksu
2, Run to open restricted folders:  gksudo nautilus


The images are stored 
Each of these layers is stored in its own directory inside the Docker host’s local storage area. To examine the layers on the filesystem, list the contents of /var/lib/docker/<storage-driver>/layers/.  


 To view the contents of Docker folder

sudo ls /var/lib/docker/

The 'overlay2' is the storage driver

To view images folder contents

sudo  ls /var/lib/docker/image/overlay2/imagedb/content/sha256/

To view containers folder contents 

sudo ls /var/lib/docker/containers/

sudo du -sh /var/lib/docker

sudo du -sh /* /var/lib/docker


To view image folder  size

sudo  du -sh /var/lib/docker/image/overlay2/imagedb/content/sha256/


To view the individual image size

sudo  du -sh /var/lib/docker/image/overlay2/imagedb/content/sha256/e8171dd5ff507b237ff004b8faec3f8e0c59b6319f97a56b19ff8f7f2907e48e

To view containers folder size

sudo du -sh /var/lib/docker/containers

To view individual container size

sudo du -sh /var/lib/docker/containers/3143b5e5b4c06047f6d6c7337070e186f92ff6f211d9a80602025fa28e85a55e


The built images storege
sudo ls  /var/lib/docker/overlay2/


From current dir

sudo du -sh * 

cd /var/lib/docker

 and run sudo du -sh * 

sudo du -sh /var/lib/docker/builder

To view the build images sizes

sudo du -sh /var/lib/docker/overlay2



To view the volume contents

sudo ls /var/lib/docker/volumes

To view the volumes folder size

sudo du -sh /var/lib/docker/volumes

To view individual volume contents

sudo ls /var/lib/docker/volumes/bf96483223832bcb7a0ca46789ef2f0a8b8d14545a32916c24883c595431bfb2


To view individual volume size

sudo du -sh /var/lib/docker/volumes/bf96483223832bcb7a0ca46789ef2f0a8b8d14545a32916c24883c595431bfb2

 To view the image repositories on local machine

sudo cat /var/lib/docker/image/overlay2/repositories.json

sudo cat /var/lib/docker/image/overlay2/repositories.json | python -mjson.tool
The output of above matches with 'docker images' command


  for each in $(ls /var/lib/docker) ; do du -hs "$each" ; done


docker search : Search the Docker Hub for images
docker search busybox

docker search --filter stars=3 busybox

docker search --filter "is-official=true" --filter "stars=3" busybox

Format the output
docker search --format "{{.Name}}: {{.StarCount}}" nginx

docker search --format "table {{.Name}}\t{{.IsAutomated}}\t{{.IsOfficial}}" nginx

 Search in private local registry

docker search localhost:5000/centos

Uisng HTTP API with curl

curl -X GET http://localhost:5000/v1/search?q=postgresql


https://docs.docker.com/v17.09/engine/userguide/storagedriver/imagesandcontainers/#container-and-layers
https://docs.docker.com/v17.09/engine/userguide/storagedriver/selectadriver/


https://docs.docker.com/storage/volumes/

https://forums.docker.com/t/where-are-images-stored/9794

http://blog.thoward37.me/articles/where-are-docker-images-stored/

https://stackoverflow.com/questions/19234831/where-are-docker-images-stored-on-the-host-machine



To install dockerfileview, please use go get.
 Download from 
https://github.com/remore/dockerfileview/releases/download/v0.1.0/dockerfileview.v0.1.0.zip


$ go get github.com/remore/dockerfileview

If you have not installed go on your system, precompiled executables are available at release page is for you. Or, simply type docker run command such as:


 OR Run the dockerfileview image
$ docker run remore/dockerfileview dockerfileview ubuntu:14.04


docker run remore/dockerfileview dockerfileview ubuntu:14.04

dockerfileview /path/to/Dockerfile

dockerfileview centos

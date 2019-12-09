https://blog.docker.com/2013/07/how-to-use-your-own-registry/

Run a local registry
Use a command like the following to start the registry container:

$ docker run -d -p 5000:5000 --restart=always --name registry registry:2

Copy an image from Docker Hub to your own registry
You can pull an image from Docker Hub and push it to your registry. 
The following pulls the ubuntu:16.04 image from Docker Hub and re-tags it as my-ubuntu, then pushes it to the local registry. Finally, the ubuntu:16.04 and my-ubuntu images are deleted locally and the my-ubuntu image is pulled from the local registry.

Pull the ubuntu:16.04 image from Docker Hub.

$ docker pull ubuntu:16.04

docker pull busybox

docker pull --all-tags fedora

docker rmi busybox

Attach console for multiple uses

docker run -a stdin -a stdout -i -t ubuntu /bin/bash

docker run -a stdin -a stdout -a stderr ubuntu /bin/ls


Tag the image as localhost:5000/my-ubuntu. This creates an additional tag for the existing image.
When the first part of the tag is a hostname and port, Docker interprets this as the location of a registry, when pushing.

$ docker tag ubuntu:16.04 localhost:5000/my-ubuntu

Push the image to the local registry running at localhost:5000:

$ docker push localhost:5000/my-ubuntu

docker images --format "{{.ID}}: {{.Repository}} {{.Tag}}"

Remove the locally-cached ubuntu:16.04 and localhost:5000/my-ubuntu images, so that you can test pulling the image from your registry. 
This does not remove the localhost:5000/my-ubuntu image from your registry.

http://localhost:5000/v2/

$ docker image remove ubuntu:16.04
$ docker image remove localhost:5000/my-ubuntu

NOW DISCONNECT YOUR INTERNET CONNECTION WIFI OR LAN

Pull the localhost:5000/my-ubuntu image from your local registry.

$ docker pull localhost:5000/my-ubuntu

Stop a local registry
To stop the registry, use the same docker container stop command as with any other container.

$ docker container stop registry
To remove the container, use docker container rm.

$ docker container stop registry && docker container rm -v registry

****************

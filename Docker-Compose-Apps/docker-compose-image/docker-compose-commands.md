Running multiple apps in one container ..?

To chnage to another sibling/cousin  directory

cd ../

Use link and volume for sharing
Docker netywork create -- with externalk nw drivers

The docker-compose up command : Builds, (re)creates, starts, and attaches to containers for a service.

Unless they are already running, this command also starts any linked services.

The `docker-compose up` command aggregates the output of each container. When the command exits, all containers are stopped. Running `docker-compose up -d`
starts the containers in the background and leaves them running.

If there are existing containers for a service, and the service's configuratin or image was changed after the container's creation, `docker-compose up` pick up the changes by stopping and recreating the containers (preserving mounted
volumes). 
To prevent Compose from picking up changes, use the `--no-recreate` flag.

If you want to force Compose to stop and recreate all containers, use the
`--force-recreate` flag.

Usage: up [options] [--scale SERVICE=NUM...] [SERVICE...]

 
This Compose file defines two services, web and redis. 
Uses an image that’s built from the Dockerfile in the current directory.
Forwards the exposed port 5000 on the container to port 5000 on the host machine. We use the default port for the Flask web server, 5000.

docker-compose up

docker-compose up  -d

docker-compose ps

To see what environment variables are available to the web service:

docker-compose run web env
To stop
docker-compose stop

To share the current project directory s reference(Shared mount volume)to the container
Add in compose file
  volumes:
     - .:/code

To run 

docker-compose  -f docker-compose.yml up -d 

curl http://192.168.99.100:4000/

Check the docker container processes

docker-compose ps

To stop and remove the containers

docker-compose -f docker-compose.yml down

#The new volumes key mounts the project directory (current #directory) on the host to /code inside the container, #allowing you to modify the code on the fly, without having to #rebuild the image.

********************************
Scaliong the service

The docker-compose scale is depreceated

docker-compose -f app-compose.yml  scale webApp1=2

docker-compose -f app-compose.yml  scale redis=2

Instead use up with --scale option

docker-compose -f docker-compose-scale.yml up -d scale web=2 scale redis=2 

docker-compose  logs

Run the individual contaienr apps
docker-compose  run -d web python app.py


Run the redis container
docker run -d --name redis -e ALLOW_EMPTY_PASSWORD=yes redis:latest


docker-compose run -d --publish 8080:5000 web python app.py

docker-compose run  --publish 8080:5000 web python app.py

To disable service ports
docker-compose run --service-ports web python app.py


docker-compose run db psql -h db -U docker

Not To start linked containers, use the --no-deps flag:

docker-compose run --no-deps web python app.py

Run multiple compose files

docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d

For dynamic ports mapping inspect the containers

docker inspect service-containerid

docker inspect --format='{{(index (index .NetworkSettings.Ports "8090/tcp") 0).HostPort}}' docker-compose-image_webApp3_1



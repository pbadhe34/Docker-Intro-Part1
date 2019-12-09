  
Run your new load-balanced app
Before we can use the docker stack deploy command init swarm manager first:

docker swarm init

docker swarm init  --advertise-addr eth1

docker swarm init  --advertise-addr eth1

We’ll get into the meaning of that command in part 4. If you don’t run docker swarm init you’ll get an error that “this node is not a swarm manager.”
Now let’s run it. You have to give your app a name.  

docker stack deploy -c docker-compose.yml tomcat-app

  Creating network tomcat-app_webnet
  Creating service tomcat-app_web


  Docker swarms run tasks that spawn containers.
  Tasks have state and their own IDs. Let’s list the services:

   docker service ls

   docker service ps <service>

    docker service ps tomcat-app_web
    docker inspect  tomcat-app_web

    docker service logs tomcat-app_web

    docker network ls
   
    docker inspect tomcat-app_webnet

    Now list all runing tomcat containers:

   docker container ls 

   docker container ls -q

To check the output in the browser or curl
  docker-machine ip : to identify ip

  curl http://192.168.99.100:8090/ several times in a row, or go to that URL http://192.168.99.100/in the browser and hit refresh a few times.You should see the host name changed in the outputs

 demonstrating the load-balancing; with each request, one of the 5 replicas is chosen, in a round-robin fashion, to respond. The container IDs will match your output from the previous command (docker container ls -q).


Docker’s support for swarms is built using a project called SwarmKit. SwarmKit tasks do not need to be containers, but Docker swarm tasks are defined to spawn them.
Let’s inspect one of these tasks, and limit the output to container ID:

docker inspect --format='{{.Status.ContainerStatus.ContainerID}}' <task>

Vice versa, you can inspect a container ID, and extract the task ID. 

 To get the task id from container id

  docker inspect --format="{{index .Config.Labels \"com.docker.swarm.task.id\"}}" 5e13047318c0
 
  Resulting task id : ujlnfgfclnmes1s8oqqf8u3ni

 Now inspect one of these tasks, and limit the output to container ID:

docker inspect --format='{{.Status.ContainerStatus.ContainerID}}' ujlnfgfclnmes1s8oqqf8u3ni  
 

  

To Scale the app
You can scale the app by changing the replicas value
 in docker-compose.yml, saving the change, and re-running 
the docker stack deploy command:

docker stack deploy -c docker-compose.yml tomcat-app

 Or
docker-compose scale tomcat-app_web=6

The scale command is deprecated. Use the up command with the --scale flag instead. 

docker-compose up --scale tomcat-app_web=5

@@**Port binding issues@@**

docker service scale <service-name=number of instances>

docker service scale tomcat-app_web=4

docker service scale tomcat-app_web=3

docker stack deploy -c docker-compose.yml tomcat-app
Docker will do an in-place update, no need to tear the stack down first or kill any containers.

docker node ls


Now, re-run docker container ls -q to see the deployed instances reconfigured. If you scaled up the replicas, more tasks, and hence, more containers, are started.

Take down the app and the swarm
Take the app down with docker stack rm:

docker stack rm tomcat-app

To remove the service. 

docker service rm service-app_web


docker inspect  tomcat-app_web

One node is runnimng
docker node ls

Take down the (node)swarm with 
docker swarm leave --force

docker node ls

Default networks
When you install Docker, it creates three networks automatically. You can list these networks using the docker network ls command:

docker network ls

docker logs <container ID>
 
Get the container ID:

docker ps
 
docker inspect <container ID>

At the bottom,under "NetworkSettings", find "IPAddress"
      docker swarm join --token SWMTKN-1-11gs7964aviglq52jwves6r8rvn12ab3mxmz9hnxo
yutc0ikt7-8u4fam9xcwqes2byl8c3w6btd 192.168.99.101:2377

Add another NODE to the swarm  
 docker swarm join \
  --token <token> \
  <myvm ip>:<port>

  
docker-machine ssh mc2 "docker swarm join --token SWMTKN-1-11gs7964aviglq52jwves6r8rvn12ab3mxmz9hnxo
yutc0ikt7-8u4fam9xcwqes2byl8c3w6btd 192.168.99.101:2377"

docker stack deploy -c docker-compose.yml swarm

Creating network swarm_webnet
Creating service swarm_web

docker service ps swarm_web

docker service scale swarm_web=5

docker stack ps swarm_web

To remove the service. 

docker service rm service-app_web

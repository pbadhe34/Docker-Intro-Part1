docker service create [OPTIONS] IMAGE [COMMAND] [ARG...] --publish <TARGET-PORT>:<SERVICE-PORT> 

docker service create --name sql-service --hostname mysql  --replicas 2 --mount type=bind,src=/var/lib/mysql,dst=/var/lib/mysql  --env MYSQL_ROOT_PASSWORD=MyRootPass123 --env  MYSQL_DATABASE=userservice --env MYSQL_USER=app-user  --env MYSQL_PASSWORD=MyRootPass123 --publish 3306:3306 mysql:5.6

docker volume create myvolume

docker volume create --opt type=nfs --opt device=:/c/Users/Prakash/Docker-User-Service/data/mysqldata sqlvolume


 docker volume ls

 docker volume inspect sqlvolume

With named volume
docker service create --name sql-service --hostname mysql  --replicas 2 --mount type=volume,source=sqlvolume,dst=/var/lib/mysql --env MYSQL_ROOT_PASSWORD=MyRootPass123 --env  MYSQL_DATABASE=userservice --env MYSQL_USER=app-user --env MYSQL_PASSWORD=MyRootPass123 --publish 3306:3306 mysql:5.6

Mount Volume from host
docker service create --name mysql  --hostname mysql  --replicas 2 --mount type=bind,src=/c/Users/Prakash/Docker-User-Service/data/mysqldata,dst=/var/lib/mysql --env MYSQL_ROOT_PASSWORD=MyRootPass123 --env  MYSQL_DATABASE=userservice --env MYSQL_USER=app-user --env MYSQL_PASSWORD=MyRootPass123 --publish 3306:3306 mysql:5.6

Without mount volume
docker service create --name sql-service --hostname mysql  --replicas 2 --env MYSQL_ROOT_PASSWORD=MyRootPass123 --env  MYSQL_DATABASE=userservice --env MYSQL_USER=app-user --env MYSQL_PASSWORD=MyRootPass123 --publish 3306:3306 mysql:5.6

Theses services crerated are standalone and donot link the containers from services togther.

docker service create --name user-service --hostname app-host --replicas 3 --publish 8090:8090 pbadhe34/my-apps:user-app 

For full service implementation use docker compose in swarm mode.
 Create service without host name assigned(Dockerassigns defaiult name)
 

docker service  ls

docker service ps user-service
docker service ps sql-service

docker service scale mysql=4
docker service scale user-service=5


docker service logs user-service

docker service logs sql-service

docker service inspect sql-service

docker service inspect user-service

docker container ls
docker service rm  sql-service

docker service rm  user-service


curl http://192.168.99.100:8090/users


Display a live stream of container(s) resource usage statistics
docker stats [OPTIONS] [CONTAINER...]

docker stats  -a


Run in background..

docker-compose up -d
 
docker service ls  : The services are NOt created here with compose up and NO replicas are created.Only one container for each service is created.

docker ps : Displays contaienrs for each service 
docker container ls






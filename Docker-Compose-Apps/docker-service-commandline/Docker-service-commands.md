docker service create [OPTIONS] IMAGE [COMMAND] [ARG...] --publish <TARGET-PORT>:<SERVICE-PORT> 

docker service create --name myservice --hostname my-host --replicas 3 --publish 8080:8090 pbadhe34/my-apps:app1 


 Create service without host name assigned(Dockerassigns defaiult name)
docker service create --replicas 3 --publish 8080:8090 pbadhe34/my-apps:app1  


docker service  ls

docker service inspect myservice

docker service logs myservice


docker service rm  myservice

curl http://192.168.99.100:8080/


Display a live stream of container(s) resource usage statistics
docker stats [OPTIONS] [CONTAINER...]

docker stats  -a

 
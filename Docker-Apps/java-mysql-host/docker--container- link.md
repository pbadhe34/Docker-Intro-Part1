 


Container linking 
Better option is to use docker-compose


To get the redis working  

docker run -d --name redis-container -h redis-host redis

Run a another container, a busybox container as shown below:

docker run -it --link redis-container:redis --name redisclient busybox

 The value provided to the link flag is sourcecontainername:containeraliasname. The value redis-container  in the sourcecontainername since that was the name that was given to our first container that launched earlier. The containeraliasname has been selected as redis and it could be any name of choice.


cat /etc/hosts

127.0.0.1       localhost
::1     localhost ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
172.17.0.2      redis redis-host redis-container
172.17.0.3      a2dfc1019cc3


ping redis


To print out the environment variables
set


Another redis client tool use
docker run -it --link redis-container:redis --name cl- redis sh

ping redis

Launch the redis client (redis-cli) and connect to our redis server (running in another container and to which we have linked) as given below:
# redis-cli -h redis
redis:6379>
ping

set myvar DOCKER

get myvar


docker run -d -p 4000:8090 --name my_container -h py-host --link redis-container:redis  test-app:v1

curl http://192.168.99.100:4000/


 
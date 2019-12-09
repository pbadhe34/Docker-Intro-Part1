 

Run MySQL 5.6 in Docker container:

 
docker run --name app-mysql -e MYSQL_ROOT_PASSWORD=MyRootPass123 -e MYSQL_DATABASE=userservice -e MYSQL_USER=app-user -e MYSQL_PASSWORD=MyRootPass123 -d mysql:5.6
 

Check the log to make sure the mysql server is running OK:
 
docker logs app-mysql

To run MYSQL with Volume specified
Create a data directory on a suitable volume on your host system, e.g. /c/Users/Prakash/mysql/mysqldata.

Run MySQL 5.6 in Docker container:

All the characters in the names of volume must be lowercase
C:\Program Files\Docker Toolbox\docker.exe: invalid reference format: repository name must be lowercase.

The Volume specified here is used across the containers start and stop and will maniatin the database state across containers and across start and stop operations.

c/Users/Prakash/Docker-User-Service/data/mysqldata

On Windows
docker run --name app-mysql --v /c/Users/Prakash/Docker-User-Service/data/mysqldata:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=MyRootPass123 -e MYSQL_DATABASE=userservice -e MYSQL_USER=app-user -e MYSQL_PASSWORD=MyRootPass123 -d mysql:5.6

 On Linux : The /mysql/data volume directory from ROOT directory gets created

docker run --name app-mysql -v /mysql/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=MyRootPass123 -e MYSQL_DATABASE=userservice -e MYSQL_USER=app-user -e MYSQL_PASSWORD=MyRootPass123 -d mysql:5.6

docker logs app-mysql

To create some initial records and tables in mysql container
 
Solution to : File not found
Copy the files from host system into the Docker container context
The cp command can be used to copy files from host to docker container and reverse.
One specific file can be copied like:

Copy the file from host machine to the container
docker cp table.sql app-mysql:/table.sql
docker cp records.sql app-mysql:/records.sql

docker cp app-sql:/user.txt data.txt
 

docker exec -it app-mysql bash

To get the mnysql database dump to output file


Multiple files contained by the folder src can be copied into the target folder using:

docker cp src/. mycontainer:/target
docker cp mycontainer:/src/. target


docker exec -it app-mysql bash
#ls
#pwd

To import and execute sql  script in container

Run these from bash terminal to import sql script file into DB

mysql -uroot -p userservice < table.sql

mysql -uroot -p userservice < records.sql

mysql -h hostname -u user database < path/to/test.sql

 
File copied to container from Host machine and ready to execute
mysql  -u root  -p userservice < table.sql

mysql  -u root  -p userservice < records.sql


mysql -uroot -p userservice -e "describe users"  

mysql -uroot -p userservice -e "describe hibernate_sequence"  

mysql -uroot -p userservice -e "select * from users"  

mysql -uroot -p userservice -e "select * from hibernate_sequence"  


mysql -uroot -p userservice -e "DROP table users"  //Enter password



mysql -uroot -p userservice -e "commit"  

File copied to container from Host machine and ready to execute
mysql  -u root  -p userservice < table.sql

mysql -uroot -p userservice -e "commit"

docker exec app-mysql sh -c 'exec mysql userservice -uroot -p"MyRootPass123" < table.sql'

docker exec app-mysql sh -c 'exec mysql -p userservice -uroot < table.sql'

docker exec app-mysql sh -c 'exec mysql -p userservice -uroot < /c/Users/Prakash/table.sql'

docker exec app-mysql sh -c 'exec pwd'

docker exec app-mysql sh -c 'exec mysql -V' 

Get the SQL DUMP to out file
docker exec app-mysql sh -c 'exec mysqldump userservice -uroot -p"MyRootPass123" > /c/Users/Prakash/table.sql'

mysql -uroot -p userservice -e "create table hibernate_sequence;"

mysql -uroot -p userservice -e "insert into hibernate_sequence values ( 1 );"
 

docker exec -it app-mysql bash

mysql -uroot -p userservice -e "select * from users"  

mysql -uroot -p userservice -e "select * from hibernate_sequence"  

mysql -uroot -p userservice -e "create table users (id bigint not null, first_name varchar(255), last_name varchar(255), user_name varchar(255), primary key (id)) engine=MyISAM;"  


Run sleect query
docker exec app-mysql sh -c 'exec mysql SELECT * from userservice.users AS Id FROM userservice.Users -uroot -p"MyRootPass123"'

 

docker exec app-mysql sh -c 'exec mysqldump userservice -uroot -p"MyRootPass123"' > /c/Users/Prakash/records.sql

 
SELECT COUNT(Id) AS Id FROM userservice.Users;

SELECT DATABASE();

SELECT VERSION();

**************************

Another way to add records at startup

Simply just put your Data.sql file (dbcreation.sql) in a folder (ie. /mysql_init) and add the folder as a volume like this:

volumes:
  - /mysql_init:/docker-entrypoint-initdb.d
The MySQL image will execute all .sql, .sh and .sql.gz files in /docker-entrypoint-initdb.d on startup.

*********************************

Start the Tomcat8 container and link thje app-mysql container to it.


docker run -d -p 8090:8080 --name tomcat8 tomcat:8.0-jre8

docker cp tomcat-users.xml tomcat8:/usr/local/tomcat/conf/tomcat-users.xml
 
docker cp ./user-service.war tomcat8:/usr/local/tomcat/webapps/user-service.war

docker stop tomcat8
docker start tomcat8

docker commit tomcat8  pbadhe34/my-apps:user-service

docker stop tomcat8

docker rm tomcat8


docker run -p 8090:8080 --name user-app --link app-mysql:localhost -d pbadhe34/my-apps:user-service
  
***************************************************************************************************

To build the user-service-app  as image and linkt to Mysql container

Run user-service application in Docker container tomcat and link to app-mysql:

  docker build -t user-service-app .

  docker build -t user-service-app:v1 .

  To Run the user-service-app image in detacheed mode
  docker run -d user-service-app:v1 

 
docker run -p 8090:8090 --name user-app --link app-mysql:mysql -d user-service-app:v1  

You can check the log by
 
docker logs user-app

curl http://192.168.99.100:8090/users
 

Open http://192.168.99.100:8090/users in browser  


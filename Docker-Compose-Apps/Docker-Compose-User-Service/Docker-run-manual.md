version: '2'
 
services:
  mysql:
    image: mysql
    container_name: test-mysql
    ports:
      - 6603:3306
    environment:
      MYSQL_ROOT_PASSWORD: "mypassword"
    volumes:
      - /storage/docker/mysql-datadir:/var/lib/mysql

docker-compose up -d

Deploying a Stack

docker volume create mysql_data

$ docker network create drupal_mysql_net --driver=bridge

$ docker run -d --name=mysql-drupal --restart=always -v mysql_data:/var/lib/mysql --net=drupal_mysql_net -e MYSQL_ROOT_PASSWORD="mypassword" -e MYSQL_DATABASE="drupal" mysql

$ docker run -d --name=drupal -p 8080:80 --restart=always -v /var/www/html/modules -v /var/www/html/profiles -v /var/www/html/themes -v /var/www/html/sites --link mysql:mysql --net=drupal_mysql_net drupal



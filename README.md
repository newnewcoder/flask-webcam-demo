Simple Flask take picture using webcam and store to Mysql Demo

# How to run

## Setup Mysql

**step 1** install mysql
    
~~~bash
docker run --name webcam_demo_db -e MYSQL_ROOT_PASSWORD=abc123 -p 3306:3306 -d mysql:5.7 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
~~~

**step 2** setup database

~~~sql
CREATE DATABASE `mydb`;
USE `mydb`;
CREATE TABLE `user_info` (
`id` integer AUTO_INCREMENT PRIMARY KEY,
`user_name` VARCHAR(30),
`pic` LONGBLOB
) ENGINE=InnoDB
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
~~~

## Run Flask app

~~~bash
pip install -r requirements.txt
./run.sh
~~~

go [http://localhost:5000](http://localhost:5000)

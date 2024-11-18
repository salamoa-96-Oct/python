version: "3.8"
services:
  mysql:
    image: mysql:latest
    container_name: mysql-container
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: root
    ports:
      - "3306:3306"
    volumes:
      - /Users/mjs/workspace/mysql:/var/lib/mysql
---
docker run -d \
  --name mysql-container \
  -e MYSQL_ROOT_PASSWORD=root \
  -v /Users/mjs/workspace/mysql:/var/lib/mysql \
  -p 3306:3306 \
  mysql:latest
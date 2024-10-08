#!/bin/bash

# Зеленая подсветка текста
GREEN='\033[0;32m'
# Красная подсветка текста
RED='\033[0;31m'
# Белая подсветка текста
NC='\033[0m'

# Зеленая подсветка текста
echo "${GREEN}Запуск установки...${NC}"

mkdir django_work_dir

cd django_work_dir

cat > .env << EOF
DEBUG=
SECRET_KEY=
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
TOKEN_ATS=
URL_ATS=
EOF

nvim .env
internal_ip=$(hostname -I | awk '{print $1}')

cat > nginx.conf << 'EOF'
worker_processes 1;

events { worker_connections 1024; }

http {
  server {
    listen 80;
    server_name 192.168.1.8;


    location / {
      allow 192.168.1.1;
      allow 192.168.1.2;
      deny all;

      proxy_pass http://web:8000;
      proxy_set_header Host $host;
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
  }
}
EOF

cat > docker-compose.yaml << 'EOF'

version: '3.9'
networks:
  django_network:
    driver: bridge

services:
  web:
    image: jagernau/django_monitoring_cms:latest
    environment:
      DEBUG: ${DEBUG}
      SECRET_KEY: ${SECRET_KEY}
      DB_NAME: ${DB_NAME}
      DB_USER: ${DB_USER}
      DB_PASSWORD: ${DB_PASSWORD}
      DB_HOST: ${DB_HOST}
      DB_PORT: ${DB_PORT}
      TOKEN_ATS: ${TOKEN_ATS}
      URL_ATS: ${URL_ATS}
    command: gunicorn suntel.wsgi:application --bind 0.0.0.0:8000
    expose:
      - 8000
    networks:
      - django_network

  nginx:
    image: nginx:latest
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    ports:
      - 80:80
    networks:
      - django_network
EOF

echo "${GREEN}Django успешно установлен.${NC}"

echo "${GREEN}Поменяйте разрешенные IP в nginx.conf${NC}"

echo "${GREEN}Поменяйте название хоста в nginx.conf${NC}"

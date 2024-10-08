# CMS на Django для работы с БД MySQL suntel

## Неоходимые предварительные установки
* Docker
* Docker Compose
* Curl
* Neovim

## Запуск

### Самостоятельным контейнером
1. Контейнер докера: `jagernau/django_monitoring_cms:latest`
    * Как его запустить: `sudo docker run -d -p 8000:8000 --env-file .env jagernau/django_monitoring_cms:latest manage.py runserver 0.0.0.0:8000`
    * Без Nginx

### Развёртывание скриптом контейнеры с ЦМС для сервера
Скрипт разворачивает docker-compose с ЦМС для сервера: Nginx, Django.
Подключаясь к базе данных MySQL.
Потребуется внести данные в `.env` во время срабатывания скрипта.

1. Запустить скрипт `curl -s https://raw.githubusercontent.com/Jagernau/django_work/exp/django_app_install.sh | sh`
    * В файле `nginx.conf` директории `django_work_dir` внесите нужные значения:
        * Измените в строке `allow` разрешённые IP-адреса
        * Измените в строке `server_name` имя вашего сервера
2. После внесения настроек в директории `django_work_dir`, запустите проект командой `sudo docker-compose up -d`
    * Если вдруг не подтягивается последняя версия контейнера:
        * Найдите его: `sudo docker images`
        * Удалите его: `sudo docker rmi <id>`
        * Запустите процесс снова: `sudo docker-compose up -d`

### Запус проекта под локальный компьютер
Потребуется установленный Python и pip
1. Скачайте репозиторий с ЦМС `git clone https://github.com/Jagernau/django_work -b exp`
2. В скаченной директории создайте виртуальное окружение для Python `python3.10 -m virtualenv env`
3. Установите зависимости `pip install -r requirements.txt` в виртуальном окружении
4. Запустите проект `python manage.py runserver 0.0.0.0:8000`
    * По необходимости напишите unit для systemd
 * Запустите процесс
 *test test

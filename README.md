# Citizen-system

 В качестве HTTP-сервера исползуется gunicorn. Конфиг для него можно найти в репе.
 
## Инструкции к запуску на дев тачке
Сервис уже запущен на тачке. Но на всякий случай.
`$ sudo systemctl start gunicorn`
В папке `/etc/systemd/system` лежит конфиг файл для gunicorn.service. При рестарте тачки сервис перезапусится.

## Инструкции по установке
Эти инструкции следует выполнить при настройке с нуля.
#### Установить нужные зависимости
`$ pip install -r requirements.txt`
#### Настройки для БД. PostgreSQL
 Установка для Ubuntu
```
$ sudo apt-get install postgresql
$ sudo -u postgres psql
```
В сессии Postgres создать БД, создать пользователя и дать ему права на БД.
```
create database DATABASE_NAME;
create user USER_NAME with encrypted password 'PASSWORD';
grant all privileges on database DATABASE_NAME to USER_NAME;
```
Все настройки для БД следует вынести в файл config.ini на место звездочек. Сам конфиг можно найти в репе. 
```
[DATABASE]
Name = DATABASE_NAME
User = USER_NAME
Password = PASSWORD
Host = HOST
Port = PORT
```
Стандартные хост и порт для PosgtreSQL: HOST=127.0.0.1, PORT=5432
#### Добавить SECRET_KEY в config.ini
Сгенерировать SECRET_KEY. Например вот тут [https://djecrety.ir/](https://djecrety.ir/).
Занести его в config.ini.
```
[BASIC]
SecretKey = GENERATED_SECRET_KEY
```
#### Выполнить миграции
`$ python3 manage.py migrate`
#### Запуск сервера
`$ gunicorn -c ../gunicorn_config.py citizen_system.wsgi`
#### Запуск тестов
`$ pytest citizen_system/tests/citizen_system_test.py`

При запуске тестов с дев тачки необходимо активировать виртуальное окружение.
`$ source ~/env/bin/activate`

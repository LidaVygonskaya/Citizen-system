# Citizen-system

### Инструкции по установке
#### Установить нужные зависимости
`$ pip install -r requirements.txt`
#### Настройки для БД. PostgreSQL
Для Ubuntu
#### Выполнить миграции
`$ python3 manage.py migrate`
#### Запуск тестов
`$ pytest citizen_system/tests/citizen_system_test.py`
#### Запуск сервера
`$ gunicorn -c ../gunicorn_config.py citizen_system.wsgi`

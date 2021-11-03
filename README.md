# Проект: Опрос

Запуск:

1 . Активируем виртульнок оеружение:

python3 -m venv venv

Windows: venv/Script/activate

Unix(Linux): source venv/bin/activate

2 . Скачиваем пакеты:

pip install -r requirements.txt

3 . Создаем базу данных:

python manage.py migrate

python manage.py create_data -to

4 . Запускаем сервер:

python3 manage.py runserver

5 . Переходим по ссылке:

http://127.0.0.1:8000/

@echo off
REM Активируем виртуальное окружение
call venv\Scripts\activate

REM Запускаем скрипт
python manage.py runserver 127.0.0.1:8003

pause

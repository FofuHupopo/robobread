@echo off
REM Создаем виртуальное окружение
python -m venv venv

REM Активируем виртуальное окружение
call venv\Scripts\activate

REM Устанавливаем зависимости
pip install -r requirements.txt

echo Виртуальное окружение настроено и зависимости установлены.
pause

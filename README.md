# Анализ данных продаж

## Описание
Проект анализа данных о продажах с использованием PostgreSQL и Python.
Загружаю данные из БД, выполняю агрегации на SQL, анализирую в pandas и визуализирую результаты.

## Инструменты
- Python 3.12
- PostgreSQL
- pandas (обработка данных)
- matplotlib (визуализация)
- psycopg2 (подключение к БД)

## Структура проекта
- db_init.sql # создание таблицы и тестовых данных
- analysis.py # основной скрипт анализа
- revenue_by_date.png # график выручки по дням
- revenue_by_category.png # график выручки по категориям
- README.md

## Как запустить

### 1. Создать виртуальное окружение
```bash
python3 -m venv venv
source venv/bin/activate
```
### 2. Установить зависимости
```bash
pip install psycopg2-binary pandas matplotlib
```
### 3. Инициализировать базу данных
```bash
psql -U YOUR_USERNAME -d YOUR_DATABASE -h YOUR_HOST -f db_init.sql
```
### 4. Запустить анализ
```bash
python3 analisys.py
```
### Так же нужно обновить переменные в analysis.py:
```python
DB_NAME = "YOUR_DATABASE"
DB_USER = "YOUR_USERNAME"
DB_PASSWORD = "YOUR_PASSWORD"
DB_HOST = "YOUR_HOST"
DB_PORT = 5432
```


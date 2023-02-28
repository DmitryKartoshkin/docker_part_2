# образ на основе которого создаём контейнер
FROM python:3.10
# рабочая директория внутри проекта
WORKDIR StocksAndProducts
# переменные окружения для python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# обновляем pip
RUN pip install --upgrade pip
# устанавливаем зависимости
COPY ./requirements.txt /StocksAndProducts/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /StocksAndProducts/requirements.txt
# копируем файлы
COPY . /StocksAndProducts
EXPOSE 8000
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

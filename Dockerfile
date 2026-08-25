FROM python:3.9-slim

WORKDIR /app

# Устанавливаем системные зависимости для mysqlclient и отключаем буферизацию
ENV PYTHONUNBUFFERED=1
RUN apt-get update \
    && apt-get install -y pkg-config default-libmysqlclient-dev build-essential \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем зависимости Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код
COPY . .

# Собираем статику (для whitenoise)
RUN python manage.py collectstatic --noinput

# Открываем порт и запускаем Gunicorn
EXPOSE 8000
CMD ["gunicorn", "suntel.wsgi:application", "--bind", "0.0.0.0:8000"]
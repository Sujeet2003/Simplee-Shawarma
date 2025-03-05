FROM python:3.11-alpine AS builder

# Install dependencies required for mysqlclient
RUN apk add --no-cache \
    mariadb-dev \
    gcc \
    musl-dev \
    python3-dev \
    libffi-dev \
    openssl-dev \
    pkgconfig

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .


# Set environment variables from the .env file
ENV DATABASE_NAME=${DATABASE_NAME}
ENV DATABASE_HOST=${DATABASE_HOST}
ENV DATABASE_PORT=${DATABASE_PORT}
ENV DATABASE_USER=${DATABASE_USER}
ENV DATABASE_PASSWORD=${DATABASE_PASSWORD}

# Collect static files
RUN python manage.py collectstatic --noinput

EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Simplee.wsgi:application"]
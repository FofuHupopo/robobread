FROM python:3.12 AS builder

WORKDIR /app

ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONUNBUFFERED=1
ENV IS_DOCKER="true"

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8082"]

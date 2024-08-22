FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3

ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONUNBUFFERED=1
ENV IS_DOCKER="true"

COPY pyproject.toml poetry.lock* /app/

RUN poetry install --no-root --no-dev

COPY . .

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8004"]

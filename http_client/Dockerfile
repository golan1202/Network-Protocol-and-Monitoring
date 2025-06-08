FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir requests prometheus_client

CMD ["python", "http_client.py"]
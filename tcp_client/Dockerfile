FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir prometheus_client

CMD ["python", "tcp_client.py"]
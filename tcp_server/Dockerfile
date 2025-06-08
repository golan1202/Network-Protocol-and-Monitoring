FROM python:3.11-slim

WORKDIR /app
COPY tcp_server.py .

RUN pip install --no-cache-dir prometheus_client

CMD ["python", "tcp_server.py"]
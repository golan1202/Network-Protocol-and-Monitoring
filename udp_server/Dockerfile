FROM python:3.11-slim

WORKDIR /app
COPY udp_server.py .

RUN pip install --no-cache-dir prometheus_client

CMD ["python", "udp_server.py"]
FROM python:3.11-slim

WORKDIR /app

COPY http_server.py metrics.py ./

RUN pip install flask prometheus_client

EXPOSE 5000

CMD ["python", "http_server.py"]
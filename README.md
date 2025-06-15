# Communication Networks Monitoring Project

This is a learning project to understand **communication networks**, **protocols**, and **monitoring** using modern tools.

I built a system with:

✅ **HTTP**  
✅ **TCP**  
✅ **UDP**  
✅ Full metrics instrumentation → Prometheus + Grafana  
✅ Dockerized architecture → client/server separation  
✅ Automation for traffic generation  
✅ Logging of packet flow and response times  



## Project Architecture

HTTP Client  -->  HTTP Server (Flask) -->  Prometheus 

TCP Client  -->  TCP Server  --> Grafana Dashboard

UDP Client  -->  UDP Server  --> Prometheus


## Components

### HTTP

- `http_server` → Flask app exposing `/metrics` for Prometheus.
- `http_client` → sends HTTP requests to server.

### TCP

- `tcp_server` → handles TCP connections, logs packets, exports metrics.
- `tcp_client` → opens TCP connections, sends structured/random data.

### UDP

- `udp_server` → handles UDP packets, sends replies, exports metrics.
- `udp_client` → sends UDP packets periodically.

### Monitoring stack

- **Prometheus** → scrapes metrics from all servers.
- **Grafana** → visualizes the collected metrics.

---

## Metrics

The servers expose the following Prometheus metrics:

| Metric                        | Description                                |
|-------------------------------|--------------------------------------------|
| `packets_total`               | Total packets received per protocol        |
| `dropped_packets_total`       | Total packets dropped per protocol         |
| `response_time_seconds_count` | Number of response time measurements       |
| `response_time_seconds_sum`   | Sum of response times (to compute average) |

## 📦 Requirements

Before running the project locally (outside Docker),
you must install Python 3.11+ and the following dependencies:

pip install -r requirements.txt

## 🚀 How to Run the Project

Make sure Docker and Docker Compose are installed in your computer.
From the root of the project, build and start all services:
docker-compose up --build

Access services:
Grafana: http://localhost:3000 (login: admin / admin)

Prometheus: http://localhost:9090

HTTP Server: http://localhost:5000

## ✅ In Prometheus do query for all three protocols (average response time):

For example average response time for udp protocol:

rate(response_time_seconds_sum{protocol="udp"}[1m]) / rate(response_time_seconds_count{protocol="udp"}[1m])

![prometheus](https://github.com/user-attachments/assets/8ed41038-63fd-4168-9b48-8909102b9ab7)

## ✅ In Grafana: 

1. Add data Source: prometheus with a connection: http://prometheus:9090, and save.
2. Go to Dashboards and import this json for Average Response Time (per Protocol).
   
   {
  "type": "timeseries",
  "title": "Average Response Time (per Protocol)",
  "datasource": {
    "type": "prometheus",
    "uid": "your-prometheus-datasource-uid"
  },
  "targets": [
    {
      "expr": "rate(response_time_seconds_sum{protocol=~\"http|tcp|udp\"}[1m]) / rate(response_time_seconds_count{protocol=~\"http|tcp|udp\"}[1m])",
      "legendFormat": "{{protocol}}",
      "refId": "A"
    }
  ],
  "fieldConfig": {
    "defaults": {
      "unit": "s",
      "decimals": 3,
      "color": {
        "mode": "palette-classic"
      }
    },
    "overrides": []
  },
  "options": {
    "legend": {
      "displayMode": "table",
      "placement": "bottom"
    },
    "tooltip": {
      "mode": "single"
    }
  }
}


3. Save.
   
   ![grafana](https://github.com/user-attachments/assets/46c7a967-4a66-4c08-95de-0d46c67ba28e)


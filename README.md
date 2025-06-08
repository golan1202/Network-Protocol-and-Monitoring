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

Example PromQL queries:

```promql
rate(packets_total[1m])

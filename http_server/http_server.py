from flask import Flask, request, jsonify
import time, random, logging
from prometheus_client import start_http_server, generate_latest
from metrics import PACKETS_TOTAL, DROPPED_PACKETS, RESPONSE_TIME_SECONDS

app = Flask(__name__)

@app.route("/", methods=["POST"])
def handle_post():
    start_time = time.time()
    if random.random() < 0.2:
        RESPONSE_TIME_SECONDS.labels(protocol="http").observe(time.time() - start_time)
        DROPPED_PACKETS.labels(protocol="http").inc()
        return '', 500  # Simulate failure

    time.sleep(random.uniform(0, 1.5))
    data = request.json
    source = request.remote_addr
    size = len(str(data).encode('utf-8'))
    PACKETS_TOTAL.labels(protocol="http").inc()
    RESPONSE_TIME_SECONDS.labels(protocol="http").observe(time.time() - start_time)

    logging.info(f"HTTP | From {source} | Size: {size} bytes")
    return jsonify({"status": "received"})

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain'}

if __name__ == "__main__":
    start_http_server(9100)  # Prometheus pulls from here
    app.run(host='0.0.0.0', port=5000)
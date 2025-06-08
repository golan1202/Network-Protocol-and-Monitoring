import socket
import time
import random
from prometheus_client import start_http_server, Counter, Histogram

# Metrics
packet_counter = Counter("packets_total", "Total packets processed", ["protocol"])
packet_drops = Counter("dropped_packets_total", "Dropped packets", ["protocol"])
response_time_hist = Histogram("response_time_seconds", "Response time", ["protocol"])

start_http_server(9102)

HOST = "0.0.0.0"
PORT = 7000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"[UDP SERVER] Listening on {PORT}")

    while True:
        data, addr = s.recvfrom(1024)
        start = time.time()

        if random.random() < 0.2:
            print("[UDP] Dropped packet")
            packet_drops.labels("udp").inc()
            continue

        packet_counter.labels("udp").inc()
        s.sendto(b"ACK-UDP", addr)
        end = time.time()
        response_time_hist.labels("udp").observe(end - start)
        print(f"[UDP] From {addr} | {len(data)} bytes | {end-start:.4f}s")
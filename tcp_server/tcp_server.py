import socket, random, time

from prometheus_client import start_http_server, Counter, Histogram

# Metrics
packet_counter = Counter("packets_total", "Total packets processed", ["protocol"])
packet_drops = Counter("dropped_packets_total", "Dropped packets", ["protocol"])
response_time_hist = Histogram("response_time_seconds", "Response time", ["protocol"])

start_http_server(9101)  # Prometheus metrics port

HOST = "0.0.0.0"
PORT = 6000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"[TCP SERVER] Listening on {PORT}")

    while True:
        conn, addr = s.accept()
        with conn:
            start = time.time()
            data = conn.recv(1024)
            if not data:
                continue

            # Simulate drop
            if random.random() < 0.2:
                print("[TCP] Dropped packet")
                packet_drops.labels("tcp").inc()
                continue

            packet_counter.labels("tcp").inc()
            conn.sendall(b"ACK-TCP")
            end = time.time()
            response_time_hist.labels("tcp").observe(end - start)
            print(f"[TCP] From {addr} | {len(data)} bytes | {end-start:.4f}s")
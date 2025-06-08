import socket
import time
import random

while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(("tcp_server", 6000))
            message = f"Hello TCP {random.randint(1, 1000)}".encode()
            s.sendall(message)
            response = s.recv(1024)
            print(f"[TCP] Received: {response.decode()}")
    except Exception as e:
        print("TCP Client Error:", e)
    time.sleep(1)
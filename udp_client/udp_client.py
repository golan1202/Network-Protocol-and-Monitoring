import socket
import time
import random

server = ("udp_server", 7000)

while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.settimeout(2)
            message = f"Hello UDP {random.randint(1, 1000)}".encode()
            s.sendto(message, server)
            response, _ = s.recvfrom(1024)
            print(f"[UDP] Received: {response.decode()}")
    except Exception as e:
        print("UDP Client Error:", e)
    time.sleep(1)
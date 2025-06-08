import requests
import time
import random

url = "http://http_server:5000/"  # Using Docker service name

while True:
    try:
        data = {"message": f"Hello {random.randint(1, 1000)}"}
        start = time.time()
        response = requests.post(url, json=data)
        elapsed = time.time() - start
        print(f"[HTTP] Status: {response.status_code}, Time: {elapsed:.4f}s")
    except Exception as e:
        print("HTTP Client Error:", e)
    time.sleep(1)
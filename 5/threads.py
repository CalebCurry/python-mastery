import time

import httpx
import threading
from queue import Queue

q = Queue(maxsize=5000)


def worker():
    while True:
        i = q.get()
        response = httpx.get("http://localhost:8000", timeout=30)
        print(i, response.json())

        q.task_done()


for _ in range(5):
    threading.Thread(target=worker).start()

for i in range(3000):
    q.put(i)

print("Continuing")

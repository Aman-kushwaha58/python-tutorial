import threading
import queue
import time
import random

BUFFER_SIZE = 5
q = queue.Queue(BUFFER_SIZE)

def producer(producer_id):
    for i in range(10):
        item = f'Item-{producer_id}-{i}'
        q.put(item)
        print(f'Producer {producer_id} produced {item}')
        time.sleep(random.uniform(0.1, 0.5))

def consumer(consumer_id):
    while True:
        item = q.get()
        print(f'Consumer {consumer_id} consumed {item}')
        q.task_done()
        time.sleep(random.uniform(0.2, 0.6))

num_producers = 2
num_consumers = 2

producer_threads = []
for i in range(num_producers):
    t = threading.Thread(target=producer, args=(i,))
    producer_threads.append(t)
    t.start()

consumer_threads = []
for i in range(num_consumers):
    t = threading.Thread(target=consumer, args=(i,), daemon=True)
    consumer_threads.append(t)
    t.start()

for t in producer_threads:
    t.join()

q.join()

print("All items have been consumed.")

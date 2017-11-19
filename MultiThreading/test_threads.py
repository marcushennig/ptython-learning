import threading
import time

def worker(sleeping_time: int) -> None:

    """thread worker function"""
    name = threading.currentThread().getName()
    print(f'{name} starting')
    time.sleep(sleeping_time)
    print(f'{name} exiting')
    return

threads = []
for i in range(10):
    thread = threading.Thread(name=f'worker {i}', target=worker, args=(i,))
    threads.append(thread)
    thread.start()

print('Main has finished')
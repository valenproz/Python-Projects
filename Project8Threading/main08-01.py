import threading
import time

def thread_1():
    while True:
        print("Thread 1 Operation")
        time.sleep(1.0)

t1 = threading.Thread(target=thread_1)
t1.start()

while True:
    print("Main Operation")
    time.sleep(2.0)
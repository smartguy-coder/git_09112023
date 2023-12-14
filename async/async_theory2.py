import time
from threading import Thread

counter = 0


def foo(number):
    for i in range(100_000):
        global counter
        value = counter
        value += 1
        some_job = [j for j in range(100)]
        counter = value
    print(f'Function {number}', counter)
 

threads = []
for i in range(1, 6):
    thread = Thread(target=foo, args=(i,))
    threads.append(thread)
    thread.start()

for th in threads:
    th.join()

print(counter)

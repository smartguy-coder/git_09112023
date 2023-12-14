import time
from threading import Thread


def do_job(number, second_arg=None):
    for i in range(10):
        print(f'From child thread 1: {i}, {number}, {second_arg}')
        time.sleep(1)


def do_job2(number, second_arg=None):
    for i in range(10):
        print(f'From child thread 2: {i}, {number}, {second_arg}')
        time.sleep(0.25)


thread1 = Thread(target=do_job, args=(1,), kwargs={'second_arg': 25})
thread2 = Thread(target=do_job2, args=(1,), kwargs={'second_arg': 200})
thread1.start()
thread2.start()


for i in range(10, 20):
    print(f'From main thread: {i}')
    time.sleep(0.3)

print('FINISH')

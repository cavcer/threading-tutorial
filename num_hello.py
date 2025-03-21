import threading
import time

start = time.perf_counter()

def hello():
    for l in "hello":
        print(l)
        time.sleep(0.5)

def nums():
    for i in range(5):
        print(i)
        time.sleep(0.5)

t1 = threading.Thread(target = hello)
t2 = threading.Thread(target = nums)

t1.start()
t2.start()

t1.join()
t2.join()

# hello()
# nums()

finish = time.perf_counter()
print(f"finish in {finish - start:.2f} secs")
print(f"finish in {finish - start:.2f} secs")
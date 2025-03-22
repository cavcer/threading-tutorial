import time
import threading
import concurrent.futures
import random

start = time.perf_counter()

def battery():
    print("battery statu is been taking for 3 second")
    time.sleep(3)
    battery = random.randint(0,100)
    #print(f"battery={battery}")
    return battery

def is_gps():
    print("gps statu is been taking for 5 second")
    time.sleep(5)
    gps = random.choice([True,False])
    #print(f"gps={gps}")
    return gps

def temperature():
    print("temp statu is been taking for 2 second")
    time.sleep(2)
    temp = random.randint(25,100)
    #print(f"temp={temp}")
    return temp

def is_camera():
    print("camera statu is been taking for 1 second")
    time.sleep(1)
    camera = random.choice(["opened","closed"])
    #print(camera)
    return camera

functions = [battery,is_gps,temperature,is_camera]
def run_function(f):
    return f()  # Fonksiyonu çağır
# threads = []

# for f in functions:
#     thread = threading.Thread(target= f)
#     thread.start()
#     threads.append(thread)

# for thread in threads:
#     thread.join()

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(run_function, functions)

    for r in results:
        print(r)



finish = time.perf_counter()
print(f"finish in {finish - start:.2f} secs")
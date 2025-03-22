import time
import threading
import concurrent.futures
import random

start = time.perf_counter()

def battery():
    print("battery statu is been taking for 3 second")
    time.sleep(3)
    battery = random.randint(0,100)
    print(battery)
    return battery

def is_gps():
    print("gps statu is been taking for 5 second")
    time.sleep(5)
    gps = random.choices([True,False])
    print(gps)
    return gps

def temperature():
    print("temp statu is been taking for 2 second")
    time.sleep(2)
    temp = random.randint(25,100)
    print(temp)
    return temp

def is_camera():
    print("camera statu is been taking for 1 second")
    time.sleep(1)
    camera = random.choices(["opened","closed"])
    print(camera)
    return camera


battery()
is_gps()
temperature()
is_camera()


finish = time.perf_counter()
print(f"finish in {finish - start:.2f} secs")
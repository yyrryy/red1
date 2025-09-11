import os
from threading import Thread
from time import sleep
import socket

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close() 
    return ip

def runserver():
    os.system('python manage.py runserver 0.0.0.0')

def lunchchrome():
    sleep(2)  # wait for server
    ip = get_local_ip()
    os.system(f'start chrome http://{ip}')

t1 = Thread(target=runserver)
t2 = Thread(target=lunchchrome)

t1.start()
sleep(2)
t2.start()


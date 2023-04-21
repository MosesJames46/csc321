import os
import time
import sys

def run_cmd(command):
    return os.system(f"start cmd /k {command}")   

def open_file(file):
    return os.system(f'start {file}')

def ipconfig():
    run_cmd('ipconfig /all | findstr DNS')
    return 0
    
def ipconfig_dns():
    run_cmd('ipconfig /displaydns')
    return 0
def notepad():
    open_file('notepad.exe')
    return 0

def net_stat():
    run_cmd('netstat')

def vent_work():
    processes = []
    for i in range(int(input('How many workers?'))):
        processes.append(open_file('python VentilatorWork.py'))

    open_file('python VentilatorSink.py')
    time.sleep(1)
    open_file('python Ventilator.py')
    
def weather_work():
    open_file('python WeatherUpdate.py')
    time.sleep(1)
    open_file('python WeatherUpdateClient.py')
def tcp_dump():
    open_file('tcpdump')
vent_work()
# net_stat()
weather_work()
# tcp_dump()


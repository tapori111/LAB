import signal
#import resource #this is for unix
import psutil 
import os
from memory_profiler import profile
import psutil.tests

@profile

def my_func():
    x = [x for x in range(1000)]
    y = [y for y in range(1000)]
    del x
    return y

my_func()
print(psutil.cpu_times())
      
for x in range(3):
    print(psutil.cpu_times_percent(interval=1))
'''
for x in range(3):
    print(psutil.cpu_times_percent(interval=1,percpu=True))
'''

print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))

print(psutil.cpu_stats())

print(psutil.cpu_freq())
print(psutil.boot_time())

print(psutil.virtual_memory())
print(psutil.swap_memory())

print(psutil.disk_partitions())
print(psutil.disk_usage('/'))

#for p in psutil.pids():
 #   print(psutil.Process(p))

print(psutil.Process().ppid)

for proc in psutil.process_iter(['pid', 'name','username']):
    print(proc.info['name'],proc.info['username'])

#print(psutil.test())
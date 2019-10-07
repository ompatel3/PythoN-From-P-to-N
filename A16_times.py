import sys
import time
import datetime


#print(sys.path)
initial = time.time()
print(initial)
i=10
while(i>0):
    print(i,end=" ")
    time.sleep(0.1)
    i=i-1
endtime = time.time()
print("\ntotal time ",round(endtime - initial,2))


local_time = time.asctime(time.localtime(time.time()))
print(local_time)

x=datetime.datetime.now()
print(x.year)
# learn how to lock resources in order to only one thread 
# accesses resources each time

import threading
import time

# global resources: data and a lock to be used by both functions
x= 1500
lock = threading.Lock()

def doubleNum():
	global x,lock
	try:
		lock.acquire() # the function tries to lock resource x
					#if it is not locked by another function
		while x<100000:
			x*= 2
			print(x)
			time.sleep(1) # just to be able to see the changes
	finally:
		print("reached maximum!")
		lock.release()


def devideNum():
	global x, lock
	try:
		lock.acquire() # the function tries to lock resource x
					#if it is not locked by another function
		while x>1000:
			x/= 2
			print(x)
			time.sleep(1) # just to be able to see the changes
	finally:
		print("reached minimum!")
		lock.release()	


t1 = threading.Thread(target=doubleNum)
t2 = threading.Thread(target=devideNum)

t1.start()
t2.start()





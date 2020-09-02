import threading
import time

def myfunction1():
	for x in range(10):
		print("ONE")
		time.sleep(1)
		

def myfunction2():
	for x in range(10):
		print("TWO")
		time.sleep(1)

t1 = threading.Thread(target=myfunction1)
t2 = threading.Thread(target=myfunction2)

t1.start()
t2.start()

# join function makes the main thread to wait the finish of the threads
t1.join()
t2.join()

print("\n")
print("another text!")

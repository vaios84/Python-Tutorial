import threading

def myfunction1():
	for x in range(10000):
		print("ONE ")

def myfunction2():
	for x in range(10000):
		print("TWO")

t1 = threading.Thread(target=myfunction1)
t2 = threading.Thread(target=myfunction2)

t1.start()
t2.start()

# join function makes the main thread to wait the finish of t2
t2.join()

print("\n")
print("another text!")

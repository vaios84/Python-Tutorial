'''
Python Daemon Thread

To start with this tutorial, you should have basic knowledge about threads. Basically there are two types of thread. One is daemon thread. Another is non-daemon thread.

While a non-daemon thread blocks the main program to exit if they are not dead. A daemon thread runs without blocking the main program from exiting. 

And when main program exits, associated daemon threads are killed too.


When Daemon Threads are useful

In a big project, some threads are there to do some background task such as sending data, performing periodic garbage collection etc. It can be done by non-daemon thread. 

But if non-daemon thread is used, the main thread has to keep track of them manually. However, using daemon thread the main thread can completely forget about this task and 

this task will either complete or killed when main thread exits.

Note that you should use daemon thread only for non essential tasks that you dont mind if it doesnt complete or left in between.

'''


import threading
import time

path = "text1.txt"
text = ""

def readFile():
	global path, text
	while True:
		with open("text1.txt", "r") as f:
			text = f.read()
		time.sleep(3)


def printLoop():
	for x in range(30):
		print(text)
		time.sleep(1)


t1 = threading.Thread(target=readFile, daemon=True)
t2 = threading.Thread(target=printLoop)


t1.start()
t2.start()


# run this script and while running change and save the content of text1.txt. 
# It is reading the file constantly in the background and prints the new text.

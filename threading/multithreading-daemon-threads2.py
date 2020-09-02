'''
Python Daemon Thread

To start with this tutorial, you should have basic knowledge about threads. Basically there are two types of thread. One is daemon thread. Another is non-daemon thread.

While a non-daemon thread blocks the main program to exit if they are not dead. A daemon thread runs without blocking the main program from exiting. 

And when main program exits, associated daemon threads are killed too.


When Daemon Threads are useful

In a big project, some threads are there to do some background task such as sending data, performing periodic garbage collection etc. 

It can be done by non-daemon thread. But if non-daemon thread is used, the main thread has to keep track of them manually. 

However, using daemon thread the main thread can completely forget about this task and this task will either complete or killed when main thread exits.

Note that you should use daemon thread only for non essential tasks that you dont mind if it doesnt complete or left in between.
'''

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

def n():
    logging.debug('Starting')
    logging.debug('Exiting')

def d():
    logging.debug('Starting')
#remove the sleep function, run again to check difference
    time.sleep(5)
    logging.debug('Exiting')

if __name__ == '__main__':

	t = threading.Thread(name='non-daemon', target=n)

	d = threading.Thread(name='daemon', target=d)
	d.setDaemon(True)

	d.start()
	t.start()

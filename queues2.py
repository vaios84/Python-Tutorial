'''
The module queue implements three types of queue, which differ only in the order in which the entries are retrieved. 
In a FIFO queue, the first tasks added are the first retrieved. In a LIFO queue, the most recently added entry is the first retrieved (operating like a stack). 

With a priority queue, the entries are kept sorted (using the heapq module) and the lowest valued entry is retrieved first.

the Constructor for a FIFO queue
class queue.Queue(maxsize=0)

the Constructor for a LIFO queue
class queue.LifoQueue(maxsize=0)

the Constructor for a priority queue
class queue.PriorityQueue(maxsize=0)

'''

import queue

#Constructor for a LIFO queue
q = queue.LifoQueue()

numbers = [10, 20, 30, 40, 50, 60, 70]

for x in numbers:
	q.put(x)

#LIFO queue will print the last two that entered the queue
print(q.get())
print(q.get())


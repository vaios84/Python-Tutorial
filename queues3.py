import queue

#Constructor for a priority queue
q = queue.PriorityQueue()

q.put((2, "hello there!"))
q.put((12, 23.55))
q.put((6, 100))
q.put((1, True))
q.put((4, "vaios"))


while not q.empty():
	print(q.get())



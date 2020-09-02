import threading

event = threading.Event()

def myFunction():
	print("waiting for event to trigger...\n")
	event.wait()
	print("performing action xyz...\n")


t1 = threading.Thread(target=myFunction)
t1.start()


x = input("do you want to trigger the event? (y/n) \n")

if x=="y" or x=="Y"
	event.set()
else:
	print("ok.. waiting.\n")



def myFunction():
	try:
		age = int(input("Age: "))
		print(age)
		income = 50000
		risk = income / age
		print(risk)
	except ZeroDivisionError: # in case the user inserts 0 as age
		print("Age cannot be 0. ") 
	except ValueError:  # in case the user inserts a string not an int
		print("Invalid error.") 

print("start")
myFunction()

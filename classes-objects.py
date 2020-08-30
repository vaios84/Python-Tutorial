
class Person: 
	
	# the constructor
	def __init__(self, name , age, height):
		self.name= name
		self.age= age
		self.height = height
	
	# with the str function I can then do print(an object)
	def __str__(self):
		return f"name: {self.name}, age: {self.age}, height: {self.height} "
	
	# the destructor
	def __del__(self):
		print("I am the destructor! Object deleted! ")
		
		



p1 = Person("Mike", 30, 178)

print(p1.name)
print(p1.age)
print(p1.height)

p1.age = 35
print("changed age:")
print(p1.age)

print(p1)


del p1


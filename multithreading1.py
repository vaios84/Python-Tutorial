# the Super-Class
class Person: 
	
	# the constructor
	def __init__(self, name , age, height):
		print("I am the super class constructor!")
		self.name= name
		self.age= age
		self.height = height
	
	# with the str function I can then do print(an object)
	def __str__(self):
		return f"name: {self.name}, age: {self.age}, height: {self.height}"
		
	def get_older(self, years):
		self.age += years
	
	# the destructor
	def __del__(self):
		print("I am the superclass destructor! Object deleted! ")
		
		

# inheritance. Worker is the Sub-Class
class Worker(Person):
	
	# the constructor
	def __init__(self, name , age, height, salary):
		super(Worker, self).__init__(name, age, height)
		self.salary = salary 
		print("I am the subclass constructor!")
		
	def calc_yearly_salary(self):
		return self.salary*12
		
	# override __str__ function
	def __str__(self):
		text = super(Worker, self).__str__()
		text += f", salary: {self.salary}" 
		return text 



worker1 = Worker("Jimmy",40, 185, 2500)

print(worker1)
print("change the age:")
worker1.get_older(5)
print(worker1.age)
	

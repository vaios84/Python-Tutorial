# create a new Class that is going to be the SuperClass
class Mammal:
	def walk(self):
		print("Walkinnn")
	
# subClass
class Dog(Mammal):
	def bark(self):
		print("barkinnn barkinnn")
	

# subClass
class Cat(Mammal):
	pass # just to keep the python interpreter happy. 
		# the pass keyword means nothing exists here, just pass this line. 
	

dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.walk()



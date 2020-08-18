# create a new Class
class Mammal:
	def walk(self):
		print("Walkinnn")
	

class Dog(Mammal):
	def bark(self):
		print("barkinnn barkinnn")
	


class Cat(Mammal):
	pass # just to keep the python interpreter happy. pass means nothing exists here, just pass this line. 
	

dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.walk()



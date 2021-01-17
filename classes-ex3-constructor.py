# create a new Class
class Point:
	def __init__(self, x, y, name): # the constructor
		self.x =x
		self.y =y
		self.name = name
	
	def move(self):
		print("movinnn")
	
	def draw(self):
		print("draw cartoons")
		
	def talk(self):
		print(f"Hello I am from {self.name}. I am new here. ")


# main function

# create Objects of the Class
p1 = Point(10, 5, "New York")
p2 = Point(8, 80, "London")

p1.talk()
p2.talk()

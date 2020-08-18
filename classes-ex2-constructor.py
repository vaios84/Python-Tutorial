# create a new Class
class Point:
	def __init__(self, x, y): # the constructor
		self.x =x
		self.y =y
	
	def move(self):
		print("movinnn")
	
	def draw(self):
		print("draw cartoons")
		
		
		
# create Objects of the Class
p1 = Point(10, 5)
p2 = Point(8, 80)

print(p1.x)
print(p1.y) 

print("P2: x= " + str(p2.x) + ", y= " + str(p2.y))

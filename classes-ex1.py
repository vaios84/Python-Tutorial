# create a new Class
class Point:
	def move(self):
		print("movinnn")
	
	def draw(self):
		print("draw cartoons")
		
		
		
# create Objects of the Class

point1 = Point()
point2 = Point()

point1.draw()
point2.move()

# We can give attributes to an object that are not described in the Class
point1.total = 100
print(point1.total)


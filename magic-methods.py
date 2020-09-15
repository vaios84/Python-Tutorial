# declare our class
class JustText:

	# magic method to initiate object (constructor)
	def __init__(self, string):
		self.string = string

	# print our string object (repr = represent)
	def __repr__(self):
		return 'Object: {}'.format(self.string)

	def __add__(self, other):
		return self.string + other

# Driver Code
if __name__ == '__main__':

	# object creation
	str1 = JustText('Hello ')
	print(str1)

	# user input
	name = input('name: ')

	# concatenate String object and a string
	print(str1 + name)

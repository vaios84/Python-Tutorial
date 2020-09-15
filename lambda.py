'''
In Python, anonymous function means that a function is without a name.
As we already know that def keyword is used to define the normal functions
and the lambda keyword is used to create anonymous functions.
It has the following syntax:
lambda arguments : expression

'''

# Python program to demonstrate
# lambda functions


x ="GeeksforGeeks"

# lambda gets pass to print
(lambda x : print(x))(x)

# calc the cube of a number
def cube(y):
    return y*y*y;

g = lambda x: x*x*x
print(g(7))

print(cube(5))

def power(n):
    return lambda a : a ** n

# base = lambda a : a**2 get
# returned to base
base = power(2)

print("Now power is set to 2")

# when calling base it gets
# executed with already set with 2
print("8 powerof 2 = ", base(8)) 

# base = lambda a : a**5 get
# returned to base
base = power(5)
print("Now power is set to 5")

# when calling base it gets executed
# with already set with newly 2
print("8 powerof 5 = ", base(8))

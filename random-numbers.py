import random

print("random float nums")
for i in range(3):
	print(random.random())
	

print("\nrandom integers")
for i in range(5):
	print(random.randint(0, 10))

print("\nSelect leader")
members = ['Vaios', 'John', 'Mary', 'Dimitra']
leader = random.choice(members)
print(leader)

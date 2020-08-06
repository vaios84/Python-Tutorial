
def phone_magic():
	phone = input("phone: ")
	# A new dictionary (key, value)
	digits_mapping= {
		"1": "One",
		"2": "Two",
		"3": "Three",
		"4": "Four",
		"5": "Five" 
	}
	output = ""
	for ch in phone:
		output += digits_mapping.get(ch, "!") + " "

	print(output)


def another_function(a, b):
	print(a*b)


print("start")
phone_magic()
print("finish")

print("#" *10)
print("start")
print("multiply integers")
x= input(">")
y= input(">")
another_function(int(x), int(y))
print("finish")

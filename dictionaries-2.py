
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

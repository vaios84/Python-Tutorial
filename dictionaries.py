# A new dictionary (key, value)
customer = {
	"name": "Vaios",
	"last": "Stergiopoulos",
	"age": 35,
	"isUser": True

}

print("Customer Name: " + str(customer.get("name")) + " " + str(customer.get("last")))
print("User: " + str(customer.get("isUser")))

# update data
customer["name"] = "Jack"
customer["last"] = "Reacher"
customer["isUser"] = False

print("update data")
print("Customer Name: " + str(customer.get("name")) + " " + str(customer.get("last")))
print("User: " + str(customer.get("isUser")))

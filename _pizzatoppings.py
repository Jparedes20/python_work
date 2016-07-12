#_pizzatoppings.py
#next code will ask for pizza toppings and will storage them in a list

_pizzatoppings=[] #empty lisy

_mt=True

while _mt:
	_topping=input("Enter topping, writhe 'quit' to end: ")
	_pizzatoppings.append(_topping)
	if _topping == "quit":
	 	_mt=False

print(str(_pizzatoppings)+" \n have been added to your pizza.")

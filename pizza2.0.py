#pizza2.0py
#passing and arbitrary number of elements of a function
#*toppings is a list thats accpets any number of arguments
#In this case *toppings is the arbitrary numer of arguments as a list

def make_pizza(size,*toppings):
	"""Preparing a pizza with a number of toppings"""

	print("Making a "+str(size)+"-inch pizza with the next ingredients:")
	for toping in toppings:
		print("-"+toping)

make_pizza(16,"ham","pinaple")
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


#_pizza.py
#creates a list of toppings inside a ditionary

_pizza={
	'crust':'thin',
	'toppings':['chese','ham','pinaple','hot sauce'], #define toppings list inside _pizza dictionary
}

print("You order a pizza with "+str(_pizza['crust'])+" crust")
print("\n And the next list of topings:\n")

for topping in _pizza['toppings']:
	print ("\t"+str(topping).title())



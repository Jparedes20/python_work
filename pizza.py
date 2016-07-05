#pizza.py
#Next code put in practice loops and lists in pythonm

_pizzas=[] #define an empty list named pizza


#add pizza types to the list
_pizzas.append("hawaian")
_pizzas.append("peperoni")
_pizzas.append("chese")
_pizzas.append("all meat lovers")

_friendpizzas=_pizzas[:]#make a copy of all elements of a list to a new list
_friendpizzas.append("ham") #adding a new element to the new list


#print(_pizzas)
print("\tMy favorite pizzas are:\n")
for pizza in _pizzas:
	print("\t"+pizza.title()+":")
	print("\t\tI love "+pizza+" pizza!")

print("\n\t\t I can say I really love pizza \n\t\tbut I have to have cold beer!! with my pizza\n\t\tthat's my only rule")

print("\n\tMy favorite pizzas are: "+str(_pizzas).upper())
print("\n\tMy friend favorite pizzas are: "+str(_friendpizzas).upper())


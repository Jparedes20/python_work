#Sorting a list() permanently with sort()

#LIst of the cars i would like to have
_dreamCars=['BMW','AUDI','MERCEDES','PORCHE','RANGE ROVER','MUSTANG']

print("\n\tThis is the list of cars I would love to drive: \n\t"+str(_dreamCars))
_dreamCars.sort()#sort() sort the list permanently

#print(_dreamCars.sort())Check this sintaxis error, compared with print(sorted(_ownCars)), where the list can
#be printed without been wrapped string()

print("\n\tThis is the list of cars but in order: \n\t"+str(_dreamCars))
print("\n\tAs you can see the list is been sorted permanently: \n\t"+str(_dreamCars))

#sort the list in reverse order with the parameter reverse=true
_dreamCars.sort(reverse=True)
print("\n\tThis is the list in reverse order: \n\t"+str(_dreamCars))


_ownCars=['ROGUE','JEEP','CHALLENGER','CHEVY']
#finding the lenght of a list with len()
print("\n\tI have: "+str(len(_ownCars))+" cars")
print("\n\tThese are the cars my family own: \n\t"+str(_ownCars))
print("\n\tThese are the cars my family own in order: \n\t"+str(sorted(_ownCars,reverse=True)))
#Notice the sorted() can take the argument reverse=True, the same as sort()
print("\n\tHere is the original list: \n\t"+str(_ownCars))

#printing a list in reverse order with reverse()
#We can print a list in reverse order without been sorted()
_ownCars.reverse()
print("\n\tWe can change the order of the list: \n\t"+str(_ownCars))


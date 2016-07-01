#Jerry Paredes
#We add,remove and modify elements of a list

_bikes=[] #Here I declared an empty list

print("\n\tBikes in my garage: \n\t"+ str(_bikes).upper()+"I have none :(")
_bikes.append('honda') #appened a bike to the list [0]
print("\n\tBut after saving some money I got \n\t"+"a "+str(_bikes[0]).upper()+" Shadow")
_bikes.append('kawasaki') #append a bike to the list [1]
print("\n\tThen a friend sold me a \n\t"+str(_bikes[1].upper()))
_bikes.append('harley') #appened a bike to the list [2]
print("\n\tBut my dream always was to ride a \n\t"+str(_bikes[-1].upper())+" DAVIDSON, so I bough one")
print("\n\tNow I have these bikes in my garage: \n\t"+ str(_bikes).upper()+" I'm happy :)")

#Insert an element to a list by index number
_bikes.insert(0,'ducati')
print("\n\tMy friend came to storage his bike in my storage \n\t"+str(_bikes).upper()+" I gave me the 1st spot")

#Removing elements of a list with del
del _bikes[0] #remove my friends bike
print("\n\tMy friend just left, he took his bike with him \n\t"+str(_bikes).upper())

#using pop() to remove elements of a list
_mario=_bikes.pop()
print("\n\tI let my friend Mario to borrow one of my bikes\n\t"+str(_bikes).upper())
print("\n\tHe thinks the American way, he chose the "+_mario.upper())
print("\n\t"+str(_bikes).upper())

#when you dont know the position of the item you want to remove from a list, but you know the value
#you can use remove()
_jhony="honda"
_bikes.remove(_jhony)
print("\n\tMy frien Jhony ask me if he can use a bike, I told him yes"+str(_bikes).upper())

_bikes.append(_mario)
_bikes.append(_jhony)
print("\n\tMario and JHony has returned the bikes to me safely\n\t"+str(_bikes).upper())

#Sort a list permanently with sort() method
_bikes.sort()
print("\n\tThis is the list of my bikes in order: "+str(_bikes).upper())

#ask for an unknown item in list
#_uknow='indian'
#_bikes.remove(_uknow)
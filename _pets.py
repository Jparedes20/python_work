#_pets.py
#remove all instances of a value from a list


pets=['cat','dog','hamster','cat','goldfish','dog','rabbit','cat']
print(pets)

#remove cat instances from the list
while 'cat' in pets:
	pets.remove('cat')

print("\ncat's are gone..")
print(pets)
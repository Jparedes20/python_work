#cities.py
#using break to exit a loop
#while True will create an infinite loop

while True:
	_city=input("Write the name of a city you would like to visit:"+
		"\nEnter 'quit' to exit: ")

	if _city == 'quit':
		break #we break the infinite loop
	else:
		print("\nI would love to go to "+_city.title()+" too!\n")
#mountain_poll
#Fillign a dictionary whit a while loop
#We create a poll dictionary and then with a loop ask users to fill the poll

_favorite_mountains={} #Create an empty dictionary

while True:
	name = input("\nWhats your name? ")
	mountain = input("\nWhat mountain would you like to climb? ")
	_favorite_mountains[name] = mountain

	repeat = input("Would you like to let another peson respond? (yes/no) ")	
	if repeat == "yes":
		continue
	else:
		break

#printing poll results
print("\n\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Poll Results\n")
for name, response in _favorite_mountains.items():
	print(str(name).title()+" would like to climb "+ str(response).title())
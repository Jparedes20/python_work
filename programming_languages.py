#programming_languages
#A dictionary of similiar objects
#In this case we want make a poll of many people and their favorite language

#create a dictionary of the poll answers
favorite_language={
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	'aldo':'java',
}

#make a list of my friends
_myfriends=['edward','jen','mario','pedro']

#print the poll results with key value
print("The results of the poll are: \n"+str(favorite_language))

#find the value of a specific key
print("\nEdward favorite programming language is: "+str(favorite_language['edward']).title())

#check the dictionary against a list of friends, if they are found in the dictionary, we present a greeting
print("\nNext we check all the names(keys) in the dictionary and if we find our friends we give a messsage:")

#check that my frinds had taken the poll
for _name in _myfriends:
	if _name in favorite_language.keys():
		print("Hi "+str(_name).title()+" I see your favorite language is "+
			str(favorite_language[_name]).title()+", mine too!!")
	else:
		print(_name.title()+", you need to take the poll!")


#looping through the values only in a dictionary with values()
#as you can notice python repeat twice
print("\nThe next languages are the most popular:")
for _lang in favorite_language.values():
	print(str(_lang.title()))

#to avoid repet values from a dictionary we use set()
#set() is similiar to a list with the exeption that each value in the list must be unique.
print("\nWe dont want repet values, so we fixed it:")
for _lang in set(favorite_language.values()):
	print(str(_lang.title()))
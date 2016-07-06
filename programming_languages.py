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

print("The results of the poll are: \n"+str(favorite_language))
print("Edward favorite programming language is: "+str(favorite_language['edward']).title())
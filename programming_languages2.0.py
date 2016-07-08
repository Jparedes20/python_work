#programming_languages2.0
#what if a user chose more than one favorite programming language
#we use lists inside a poll dictionary to save this languages

favorite_languages={
	'jen':['python','perl','bash'],
	'sarah':['c','c#'],
	'edward':['ruby','perl'],
	'phil':['python'],
	'aldo':['java','c#','php'],
}

for name, languages in favorite_languages.items():
	#we check if the list of languages contains more than 1 element before looping
	if len(languages) >  1:
		print("\n"+str(name).title()+"'s favorite languages are:\n\t")
		for language in languages:
			print(language)
	else:
		#if the list only contains one language, there is not need of looping, so we print the first value[0] only
		print("\n"+str(name).title()+"'s favorite language is:"+str(languages[0]).title()+"\n\t")
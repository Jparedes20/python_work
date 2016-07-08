#users2.0
#we nest a dictionary inside a dictionary

_users={#define main dictionary
	#define a sub dictionary with key=username ans its values {},
	'ntesla':{
		'firstn':'nikola',
		'lastn':'tesla',
		'dob':'07/10/56',
		'place':'croatia',
	},
	'aeinstein':{
		'firstn':'albert',
		'lastn':'einstein',
		'dob':'03/14/79',
		'place':'germany',
	},
	

}

#print values inside the dictionary
for uname,user_values in _users.items():
	print("\n\n\tUser name: "+str(uname))
	print("\n\t\tFull name: "+str(user_values['firstn']).title()+" "+str(user_values['lastn']).title())
	print("\n\t\tDate of birth: "+str(user_values['dob']).title())
	print("\n\t\tCountry: "+str(user_values['place']).title())



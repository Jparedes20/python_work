#contacts.py
#next code saves contacts phone numbers in a dictionary

_contacts={
	'mario':'832-814-6883',
	'lucy':'832-921-5600',
	'jessica':'832-614-3580',
	'gerardo':'713-261-9356',
	'samy':'281-707-5701',
}

#looping through a dictionary of the same key values
for contact in _contacts:
	print(str(contact).title()+": "+str(_contacts[contact]))

#another way of looping through the contacts with items()

for _name,_number in _contacts.items():
	print(str(_name).title()+": "+str(_number))

#now we loop through the keys only with keys()

print("\nThese are the names of my contacts:")
#for _name in _contacts.keys():
for _name in _contacts:#keys() is the default behavior
	print(_name)





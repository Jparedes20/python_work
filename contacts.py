#contacts.py
#next code saves contacts phone numbers in a dictionary

_contacts={
	'mario':'832-814-6883',
	'lucy':'832-921-5600',
	'jessica':'832-614-3580',
	'gerardo':'713-261-9356',
	'samy':'281-707-5701',
}

for contact in _contacts:
	print(contact +": "+str(_contacts[contact]))


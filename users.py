#users.py
#we loop though a dictionary with different key values

user_0={
	'username':'csantana',
	'fname':'carlos',
	'lname':'santana',
	'dob':'07/12/1965',
}

#looping and printing each key value with items()

for _key, _value in user_0.items():
	print(_key+": "+_value)

#notice the the key values are not returned in order
#to make them print in order we use sorted()


for _key in sorted(user_0.keys()):
	print(_key)
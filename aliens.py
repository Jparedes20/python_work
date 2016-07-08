#aliens.py
#In python we can nest list inside of lists, lists inside dictionaries, dictionaries inside lists and so on.

alien_0={
	'color':'green',
	'speed':'slow',
	'points':'5',
}

aliend_1={
	'color':'yellow',
	'speed':'medium',
	'points':'10',
}

aliend_2={
	'color':'red',
	'speed':'high',
	'points':'20',
}

_aliens=[alien_0,aliend_1,aliend_2] #a list with 3 dictionaries

#we loop through the list of dictionaries.
for alien in _aliens:
	print(aliens)
	
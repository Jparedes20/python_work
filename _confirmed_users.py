#_confirmed_users.py

_rsvp=[]
_friends=['jhony','mario','pedro','tony']

#I will confirm which user will come to my party

while _friends:
	_dude=_friends.pop()

	print(str(_dude).title()+" is comming to the party!")
	_rsvp.append(_dude)

print("\n\n\tFriends RSVP:")
for friend in _rsvp:
	print(str(friend).title())

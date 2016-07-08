#aliens2.py
#we crete aliens faster with range()

#making an empty list to storage aliens.
_aliens=[]

#making a list of 30 green aliens
_idnumber=0 
for _newalien in range(30):
	_newalien={
		'id':'',
		'color':'green',
		'points':'5',
		'speed':'slow',
	}
	_newalien['id']=str(_idnumber)
	_aliens.append(_newalien)
	_idnumber=_idnumber+1

#print the first 5 aliends
for alien in _aliens[0:5]:
	print("Alien_"+str(alien['id']))
	print(alien)

#modify the next 5 aliens of color
for alien in _aliens[6:11]:
	if alien['color']=="green":
		alien['color']='yellow';
		alien['points']='10'
		alien['speed']='medium'
	print(alien)

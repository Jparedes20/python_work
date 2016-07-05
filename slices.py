#We play with slices of lists

#slicing a list

#we have a list with soccer playes
_splayers=['messi','cr7','luis suarez','casillas','neymar']
print("\n\tThese are my favorite players of the spanish league: \n\t"+str(_splayers).upper())
print("\n\tThe first three players are: \n\t"+str(_splayers[0:3]).upper())
print("\n\tThe middle players are: \n\t"+str(_splayers[1:4]).upper())

print("\n\tThe last two players are: \n\t"+str(_splayers[-2:]).upper())

#copying lists
_marioplayers=_splayers[:] #we copy a list with the same elements
print("\n\tThese are my friend Mario fav players of the spanish league: \n\t"+str(_marioplayers).upper())

_marioplayers.append("cavani")
_splayers.append("slathan")

print("\n\tI have a new fav player: \n\t"+str(_splayers).upper())
print("\n\tMario has a new fav player too: \n\t"+str(_marioplayers).upper())

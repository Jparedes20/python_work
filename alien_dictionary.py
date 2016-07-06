#alien_dictionary
#we create dictionaries with python, modify key values, print key values etc

alien_0 = {} #define an empty dictionary

alien_0['color']="green"
alien_0['points']="5"
alien_0['speed']="medium"
alien_0['x_postion']="10"
alien_0['y_position']="20"

print("We print the current valies of the alien_0: \n\t"+str(alien_0))

#lets assume that you shoot down alien_o, how many point will you get
print("\n YOu shoot down alien_0 you have: "+str(alien_0['points'])+" points.")

#we change the color of alien_0 to red since now is bleeding
alien_0['color']="red"
print("\n NOw the alien_0 is dying and is color: "+str(alien_0['color'])+".")

#determine the alien position
print("\n The poriginal alien_0 position were: x="+str(alien_0['x_postion'])+" y="+str(alien_0['y_position']))

if alien_0['speed'] == "slow":
	x_increment = 5
elif alien_0['speed'] == "medium":
	x_increment = 10
else:
	#must be fast alien
	x_increment = 20

#in next code I had to warpp the str x_position into an int object in way to add them	
alien_0['x_postion']=int(alien_0['x_postion']) + x_increment
print("\n The new alien_0 position were: x="+str(alien_0['x_postion'])+" y="+str(alien_0['y_position']))



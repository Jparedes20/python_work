#checking logged users with condictionals

#define a list with all the users in the system
_users=[]
#_users=['jparedes','monaco','barca10','messid10s','admin']

if (len(_users)<1):
	print ("Zero users registered")
else:
	for user in _users:
		if (user=="admin"):
			print("HI Admin, tell me what would you like to check first?")
		else:
			print ("Welcome "+str(user)+ "It's been a while")	
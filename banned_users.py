#checking a value in a list with if statements.

banned_users=['andrew','carolina','jerry','david']
_buser="david"

if _buser not in banned_users:
	print (_buser.title() + ", you are alowed to make a post")
else:
	print("You are banned from the system!")

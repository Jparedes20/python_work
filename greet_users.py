#greet_users.py
#a list is passed to the function 

def greet_users(names):
	"""Print a simple greeting to each user in the list."""
	for name in names:
		print("Hello "+str(name).title()+"!")


#Here we define the list that we are going to pass to the function
friends_list=['mario','carlos','juan']
greet_users(friends_list)
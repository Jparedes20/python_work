#user_profile.py
#define an arbitrary function which you can pass a dictionary

def build_user(fname,lname,**user_info):
	"""BUilding a dictionary containing everything we know about the user"""

	user_profile={}
	user_profile['first_name']=fname
	user_profile['last_name']=lname
	for k, v in user_info.items():
		user_profile[k]=v

	return user_profile

user_profile=build_user("Albert","Einsten",location="princeston",field="physics")
print(user_profile)
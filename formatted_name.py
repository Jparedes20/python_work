#formatted_name.py
#we return value from a funtion

def formatted_name(_fname,_lname,_mname=""):
	if _mname:
		full_name=_fname+" "+_mname+" "+_lname
	else:
		full_name=_fname+" "+_lname

	return full_name.title()

musician=formatted_name("jimmy","hendrix")
print(musician)

musician=formatted_name("john","hooker","lee")
print(musician)
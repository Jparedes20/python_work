#build_person.py
#we use a function called build_person to create objects(humans)

def create_human(_fname,_lname,_sex,_weight,_mname="",_age=""):
	human={}#create a dictionary

	if _mname:
		full_name=_fname+" "+_mname+" "+_lname
	else:
		full_name=_fname+" "+_lname

	#we just creat a human
	human={'name':full_name,'sex':_sex,'weight':_weight}

	if _age:
		human['age']=_age

	return human

#we will create a human
print(str(create_human("jessica","sanchez","female","160","maria",30)).title())
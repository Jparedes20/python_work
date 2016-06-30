#Integers and Floats in python

_age=30 #Integer
_name="carlos"

#This code will generate an error, because you cannot convert a integer object to string implicitly

#print("Hello "+_name.title()+ "you are "+ _age) 
print("Hello "+_name.title()+ "you are "+ str(_age)+" years old!")


#Area of a circunference
_pi=3.1416
_radios=23.5
_area=(_pi*(_radios**2))
print(_area)

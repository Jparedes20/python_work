#Working with numbers in python

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

#Using range() to make a list() of numbers

print("List of numbers:\n"+str(list(range(1,14))))#This code will print a list of numbers
print("\neven numbers:\n"+str(list(range(2,14,2))))#This code will print all even numbers in the list
print("\nThere is a total of: "+str(len(list(range(2,14,2))))+" even numbers")
print("\nOdd numbers in the list:\n"+str(list(range(1,14,2))))#This code will print all odd numbers in the list
print("\nThere is a total of: "+str(len(list(range(1,14,2))))+" odd numbers")

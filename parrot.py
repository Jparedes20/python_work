#parrot.py
#first input()

_prompt=input("myprompt#") #we define a prompt with input()
print(_prompt)

#take values from a user and storage them in a dictionary
_amigo={
	'name':'',
	'age':'',
	'origin':'',
	'work':'',
} #create an empy dictionary only with keys

_amigo['name']=input("\nWhats your name amigo: ")
_amigo['age']=input("How old are you: ")
_amigo['origin']=input("Where are you from: ")
_amigo['work']=input("What do you do for leaving: ")

print("\n\tLet me make sure I got everything right: \n")
print("\tYour name is: "+str(_amigo['name']))
print("\tYou are: "+str(_amigo['age'])+" years old")
print("\tYou are from: "+str(_amigo['origin']))
print("\tAnd you are a: "+str(_amigo['work']))

	
_prompt=input("\n\tAm I right?")



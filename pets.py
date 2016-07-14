#pets.py
#We try python def to define functions for first time

#we define the functions that accept two arguments
#notice we give a default value to animal_type
#a default argument must be located at the end.
def describe_pet(pet_name, animal_type='dog'):
	print("I Have a "+animal_type+".")
	print("My "+animal_type+" name is "+pet_name.title())

#Call the function
describe_pet('max','dog')

#describe_pet('max','cat') 
#notice how the order matters when passing arguments

#using keywords arguments to avoid mistakes
describe_pet(animal_type="hamster", pet_name="ragnar")

#we call the function just with the pet_name argument, since animal_type is default to dog
describe_pet('goku')


#printing_modules
#simulate a 3d printer
#we pass a list to a function

#list of objects that need to be printed
unprinted_designs=['guitar','triangle','speaker']
complete_models=[]

#3d printer function
def print_modules(unprinted_designs, complete_models):
	"""Simulates printing each design, until  none are left."""
	"""Move each design to complete_models after printing"""

	while unprinted_designs:
		current_designs=unprinted_designs.pop()
		print("Printing "+current_designs.title()+ " modele")
		complete_models.append(current_designs)

#show function
def show_complete_modules(complete_models):
	"""Show all the modules that were printed"""
	print("\nThe following modules have been printed:")
	for modele in complete_models:
		print(modele.title())

#call functions
#we passed a copy of the list to be printed
print_modules(unprinted_designs[:],complete_models)
show_complete_modules(complete_models)
print("\nTHe original list to print was: "+str(unprinted_designs))
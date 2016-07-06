#Tuples
#Tuple is a list whcih values of the list can't been changed.

#defining a tuple ()
print("\n\tOriginal Italian Menu")
_menu=('italian trio','spaguetti with meatballs','lassagna','fetuccini alfredo')
for plate in _menu:
	print(plate)


print("\n\tModified Italian Menu")
#_menu[0]="tiramisu" #tuple objects does not support item assignment
#the only way is to change the variable that hold the list
_menu=('italian trio','spaguetti with meatballs','lassagna','fetuccini alfredo','tiramisu')
for plate in _menu:
	print(plate)


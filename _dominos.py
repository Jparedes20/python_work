#checking statements

request_toppings=['ham','pinaple','hot sauce']
_available_toppings=['ham','pinaple','peperoni','salami']

#adding all ingredients 
for _toping in request_toppings:
	if _toping not in _available_toppings:
			print("We are out of: \""+str(_toping)+"\", Sorry!")
	else:
			print("Adding "+_toping)

print("finish maing your pizza!")

#checking if the ingredients match a hawaina pizza
if ("ham" in request_toppings) and ("pinaple" in request_toppings):
	print("Enjoy your hawaian pizza!")
#_pizzeria.py
#We prepare a pizza with the requested topoing by the client,
#but if we don't have such a toping in stock,
#we let the customer know 

_request_toppings=['chese','ham','pinaple','hot sauce'] #hawaina pizza
_availabe_toppings=['chese','ham','peperoni','beef','pinaple']

for rtoping in _request_toppings:
	if rtoping in _availabe_toppings:
		print("Adding "+str(rtoping).title()+ " to your pizza")
	else:
		print("Sorry we are out of "+str(rtoping).title()+" !!")

print("Your pizza is ready!")
#_admission.py
#Checks your age and define how much you should pay to enter to a atractions park

_age=12 #define age variable ans assign value

#notice how we never use an else statement after if, python does't required.
if _age < 4 :
	_price = 0
elif _age < 18 :
	_price = 10
elif _age < 65 :
	_price = 20
elif _age >= 65 :
	_price = 10

print("Your admisnion cost is $"+str(_price)+" dollars.")
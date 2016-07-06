#conditionals on test

_age=65


if _age <= 6:
	_price=0
elif _age <=60:
	_price=10
else:
	_price=5

print("Your admission cost is: $" +str(_price)+ ".")
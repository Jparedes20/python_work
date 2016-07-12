#conditionals on test


_age=int(input("What's your age: "))

if _age < 3:
	_ticket_price=0
elif (_age >= 3) and (_age <= 12):
	_ticket_price=10
else:
	_ticket_price=15

print("Your admission cost is: $" +str(_ticket_price)+ ".")
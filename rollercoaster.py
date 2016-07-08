#rollercoaster.py
#we check the height of children before accessing the rollercoarter, if theya are higher than 38 inches
#they are allowe to access
#in this code we use int() to wrao a string and make the condition posible

_height=int(input("How tall are you in inches?: "))
if _height >=38:
	print("\nYou're tall enough, you can pass!")
else:
	print("\nYou cannot ride at this time")
	
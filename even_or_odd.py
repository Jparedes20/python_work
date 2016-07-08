#even_or_odd.py
#tells you if a number is pair or not using the % operator
import os #import os library

_exit=True

while _exit:
	os.system('clear') #clear the screen

	_number=int(input("Tell me a number and I will tell you if it is even or odd: "))
	
	if _number % 2 == 0:
		print(str(_number)+" is even!")
	else:
		print(str(_number)+" is odd!")

	_msg=input("DO you wanna try one more time? [y/n] ")
	if _msg=="y":
		_exit=True
	else:
		_exit=False


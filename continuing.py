#continuing.py
#this code makes use of the continue
#we print the odd numbers in a list 

_current_number=0
while _current_number < 10:
	_current_number += 1

	if _current_number % 2 == 0:
		continue #continue wull restart the while loop
	else:
		print(_current_number)

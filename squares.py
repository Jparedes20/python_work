#print the squares of a list of numbers

#define the list
_squares=[]
_values=list(range(1,21))

print("\nWe print a list of 20 numbers: \n"+str(_values))

#next loop will create the square of each number and will be appended to the list
for value in _values:
	_squares.append(value**2)

print("\nWe print the squares of each number in the list: \n"+str(_squares))

#simple statistics with numbers
print("\nThe lower number in the list os squares is: "+str(min(_squares)))
print("\nThe Bigger number in the list os squares is: "+str(max(_squares)))
print("\nThe sum of all the square numbers is: "+str(sum(_squares)))

#Creating comprehensions
#It is possible to create comprehensions, which combines the foor loop and the creation of new elements
#in a single line

_cubes=[value**3 for value in _values]
print("\nWe print the cubes of each number in the list: \n"+str(_cubes))






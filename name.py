#name.py 
#CHanging Case in a string with title() upper() lower() methods.
#Concatenating strings and using escape characters \n\t
#Stripping withe spaces with lstrip() rstrip()


_name='gerardo paredes'
print ("MY name with title() method: \n\t"+_name.title()) #title method
print ("MY name with upper() method: \n\t"+_name.upper()) #upper case letters
print ("MY name with lower() method: \n\t"+_name.lower()) #lowercase letters

#concatenating strings

_fname="james"
_lname="bon"
print("\n\nMy names is \n\t"+_lname.title()+" "+_fname.title()+" "+_lname.title())

#stripping whitespaces
_favorite_language="  python" #Make note that this string hasd a space in the begining.
print("\n\n"+_favorite_language+" this string has extra spaces at the beginnig.")
print(_favorite_language.lstrip()+" the extra spaces has been deleted with lstrip()")

print("\t\tAlber Eintein once said, 'A person who naver made a \n\t\tmistake never tried anything new.' ")

_fav_os="'LInux "
print(_fav_os+"Original string has an extra space at the end")
print(_fav_os.rstrip()+"Extra space has been deleted with rstrip()")

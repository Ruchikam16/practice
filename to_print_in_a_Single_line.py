Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> for each in ("Ruchika is a hero")
SyntaxError: invalid syntax
>>> for each in ("Ruchika is a hero"):
	print each,
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(each, end=" ")?
>>> for each in ("Ruchika is a hero"):
	print (each,)

	
R
u
c
h
i
k
a
 
i
s
 
a
 
h
e
r
o
>>> for each in ("Ruchika is a hero"):
	print (each, )

	
R
u
c
h
i
k
a
 
i
s
 
a
 
h
e
r
o
>>> for each in ("Ruchika is a hero"):
	print (each ,)

	
R
u
c
h
i
k
a
 
i
s
 
a
 
h
e
r
o
>>> for each in ("Ruchika is a hero"):
	print ('each',)

	
each
each
each
each
each
each
each
each
each
each
each
each
each
each
each
each
each
>>> for each in ("Ruchika is a hero"):
	print (each,end=" ")

	
R u c h i k a   i s   a   h e r o 
>>> 

x=int(input("Enter 1st number"))
y=int(input("Enter 2nd number"))
z=int(input("Enter 3rd number"))
if(x>y):
	if(x>z):
		print(x," is biggest")
	else:
		print(z," is biggest")
else:
	if y>z:
		print(y," is biggest")
	else:
		print(z," is biggest")
		
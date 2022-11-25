def longest():
	a=input("enter a list of words").split()
	h=0
	for i in a:
		c=0
		for j in i:
			c=c+1
		if c>h:
			h=c
	print("Length of longest word is: ",h)	
longest()

current=2022
n=int(input("Enter a year:"))
for i in range(current,n):
	if i%4==0:
		if i%100==0:
			if i%400==0:
				print(i)
		else:
			print(i)

import math
n=int(input("Enter the starting range: "));
m=int(input("Enter the ending range: "));
a=[]
b=[]
def even():
	for i in range(n,m):
		k=i
		flag=0
		while i>0:
			d=i%10
			if d%2!=0:
				flag=1
				break
			else:
				i=i//10
		if flag==0:
			a.append(k)
	for j in a:
		s=(int(math.sqrt(j)))*(int(math.sqrt(j)))
		if s==j:
			b.append(j)
	print(b)
even()

		

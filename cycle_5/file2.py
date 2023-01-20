f=open('test.txt')
f2=open('test2.txt','w')
p=0
for i in f:
	if(p%2==0):
		f2.write(str(i))
	p=p+1
f.close()
f2.close()
f2=open('test2.txt','r')
for i in f2:
	print(i)

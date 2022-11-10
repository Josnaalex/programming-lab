list1=list(input("enter list1 colors:").split(" "))
list2=list(input("enter list2 colors:").split(" "))
c=[]
for i in list1:
	if i not in list2:
		print(i)
	
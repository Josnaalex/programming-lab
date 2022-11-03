d={}
n=int(input("enter the no:of items"))
for i in range(n):
    key=input("enter key:")
    value=input("enter value")
    d[key]=value
d3=sorted(d.items())
print(d3)

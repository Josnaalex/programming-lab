
dict1={}
n=int(input("enter no of items:"))
for i in range(n):
    key=input("enter key:")
    value=input("enter value:")
    dict1[key]=value
print(dict1)

dict2={}
n=int(input("enter no of items:"))
for i in range(n):
    key=input("enter key:")
    value=input("enter value:")
    dict2[key]=value
print(dict2)
d3={**dict1,**dict2}
for k,v  in d3.items():
    if k in dict1 and k in dict2:
        d3[k]=[v,dict1[k]]
print(d3)



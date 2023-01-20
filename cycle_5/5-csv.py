import csv
from csv import DictWriter

dic=[{"Brand":"Apple","Model":"iphone"},
     {"Brand":"Apple","Model":"iphone"},
     {"Brand":"Apple","Model":"iphone"},
     {"Brand":"Apple","Model":"iphone"}]
     
with open("test2.csv",mode="w") as file1:
	filedict=DictWriter(file1,fieldnames=["Brand","Model"])
	filedict.writeheader()
	filedict.writerows(dic)
	
file1.close()

with open("test2.csv",mode="r") as file1:
	csvfile=csv.reader(file1)
	for x in csvfile:
		print(x)
file1.close()
	

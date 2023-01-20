import csv
with open ("testcsv.csv",mode="r") as file1:
	file1csv=csv.reader(file1)
	for x in file1csv:
		print(x)

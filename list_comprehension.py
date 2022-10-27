list1 = input("Enter integer list: ").split()
integer_list = [int(x) for x in list1]

words = input("Enter the word: ")
vowels = "AaEeIiOoUu"

square = [x*x for x in integer_list]

positive_list = [item for item in integer_list if item > 0]

vowel_list = [word for word in words if word in vowels ]

print(square)
print(positive_list)
print(vowel_list)
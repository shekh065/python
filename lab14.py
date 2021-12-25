#14.Write a Python script to check if a given key already exists in a dictionary.
A={1: 'shekh', 2: 'md', 3: 'sita', 4: 'ram', 5: 'Softwarica', 6: 'Acadamic',7:"Requirement"}
B=int(input("enter the number: "))
if B in A:
    print("present")
else:
    print("Not Present")
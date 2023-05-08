#2. Write a Python program which accepts a sequence of comma-separated numbers from userand generate a list and a tuple with those numbers.

values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('list of numbers are : ',list)
print('Tuple of numbers are : ',tuple)

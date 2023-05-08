#Write a Python program to get the difference between the two lists.
list1 = [1, 2, 3, 4]
list2 = [2, 3, 5]
difference = list(set(list1) - set(list2))
print(difference) 
#Write a Python program to check whether a specified value is contained in a group of values.Test Data :3 -> [1, 5, 8, 3] : True-1 -> [1, 5, 8, 3] : False
value1 = 3
group1 = [1, 5, 8, 3]

value2 = -1
group2 = [1, 5, 8, 3]

if value1 in group1:
    print(f"{value1} -> {group1} : True")
else:
    print(f"{value1} -> {group1} : False")

if value2 in group2:
    print(f"{value2} -> {group2} : True")
else:
    print(f"{value2} -> {group2} : False")

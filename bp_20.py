#Write a Python program to sort three integers without using conditional statements andloops.
a = 10
b = 5
c = 8
minimum = min(a, b, c)
maximum = max(a, b, c)
middle = (a + b + c) - minimum - maximum
print(minimum, middle, maximum)

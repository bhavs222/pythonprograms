#Write a Python program to count the values associated with key in a dictionary
data = {
    "A": [1, 2, 3],
    "B": [4, 5],
    "C": [1, 3, 5, 7]
}

key = "A"

count = data.get(key, [])
count = len(count)

print("Count:", count)

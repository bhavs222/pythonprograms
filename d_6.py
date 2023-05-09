#6. Write a Python program to remove a key from a dictionary.
my_dict = {"apple": 5, "banana": 3, "orange": 2}
key_to_remove = input("Enter the key to remove: ")
if key_to_remove in my_dict:
    del my_dict[key_to_remove]
    print(f"The key '{key_to_remove}' has been removed from the dictionary.")
print(my_dict)

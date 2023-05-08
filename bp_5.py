#Write a Python program to print the calendar of a given month and year.Note : Use 'calendar' module.
import calendar
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
print(calendar.month(year, month))

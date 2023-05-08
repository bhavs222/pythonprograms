#Write a Python program to calculate number of days between two dates.Sample dates : (2014, 7, 2), (2014, 7, 11Expected output : 9 days
from datetime import date
date1 = date(2014, 7, 2)
date2 = date(2014, 7, 11)
days = (date2 - date1).days
print(f"{days} days")

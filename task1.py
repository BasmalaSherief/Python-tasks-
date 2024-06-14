#!/usr/bin/python3


#Write a Python program to count the number 4 in a given list
numbers = [1,4,6,7,4]
y = numbers.count(4)
print(y)



#Write a Python program to test whether a passed letter is a vowel or not
vowels = ["a","e","i","o","u","A","E","I","O","U"]
lettercheck = input("Enter a letter: \n ")
if lettercheck in vowels:
    print("Letter entered is a VOWEL")
else:
    print("not Vowel")



#Write a python program to access environment variables
import os
import pprint
path = os.environ
pprint.pprint(dict(path),width=1)



#Write a Python program which accepts the radius of a circle from the user and compute the area
import math
R = float(input("Enter the radius: \n"))
Area = float(math.pi * R**2)
print("Area = {}".format(Area))



#Print the calendar of a given month and year
import calendar
mm = int(input("Enter a month:\n "))
yy = int(input("Enter a year:\n "))
cal = (calendar.month(yy,mm))
print(cal)

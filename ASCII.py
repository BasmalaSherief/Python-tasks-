#!/usr/bin/python3

character = input("Enter the character you want its ASCII value\n")

if len(character) != 1:
    print("not vaild, please enter 1 character")
else:
    ASCII = ord(character)
    print(ASCII)


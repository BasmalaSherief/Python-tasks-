#!/usr/bin/python3

#Ports registers
DDRA = 0b00000000

DDRB = 0b00000000

DDRC = 0b00000000

DDRD = 0b00000000

port = input("Choose which Port: \n")
bit = int(input("Enter the bit: \n"))
mode = bool(input("Mood (0 input, 1 output): \n"))

if port == "A" or port == "a":
    DDRA |= (mode<<bit)
    print(f"Port after setting {DDRA:08b}")

if port == "B" or port == "b":
    DDRB |= (mode<<bit)
    print(f"Port after setting {DDRB:08b}")
    
if port == "C" or port == "c":
    DDRA |= (mode<<bit)
    print(f"Port after setting {DDRC:08b}")
    
if port == "D" or port == "d":
    DDRA |= (mode<<bit)
    print(f"Port after setting {DDRD:08b}")

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastgd = abs(number) % 10

if (number < 0):
    lastgd = - lastgd

if (lastgd > 5):
    print(f"Last digit of {number} is {lastgd} and is greater than 5")
elif (lastgd < 6 and lastgd != 0):
    print(f"Last digit of {number} is {lastgd} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {lastgd} and is 0")

#!/usr/bin/python3
# Author - Tolulope Fakunle
for number1 in range(0, 10):
    for number2 in range(number1 + 1, 10):
        if number1 == 5 and number2 == 6:
            print("{}{}".format(number1, number2))
        else:
            print("{}{}".format(number1, number2), end=", ")

#!/usr/bin/python3
def uppercase(str):
    for i in str:
        x = i
        if ord(x) >= 97 and ord(x) <= 122:
            x = chr(ord(i) - 32)
        print("{}".format(x), end="")
    print()

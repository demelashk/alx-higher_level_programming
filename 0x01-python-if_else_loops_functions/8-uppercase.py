#!/usr/bin/python3
def upper(char):
    if ord(char) >= 97 and ord(char) <= 122:
        return (ord(char) - 32)
    else:
        return ord(char)


def uppercase(string):
    str_ing = ""
    for char in string:
        str_ing += "%c" % upper(char)
    print("{:s}".format(str_ing))

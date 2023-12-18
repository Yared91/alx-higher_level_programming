#!/usr/bin/python3
from sys import stderr

def safe_function(fct, *args):
    try:
        return fct(*args)
    except (ZeroDivisionError, IndexError, TypeError, ValueError) as ex:
        stderr.write("Exception: {}\n".format(ex))
        return None

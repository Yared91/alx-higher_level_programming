#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(val):
    try:
        print("{:d}".format(val))
        return (True)
    except (TypeError, ValueError) as ex:
        stderr.write("Exception: {}\n".format(ex))
        return (False)

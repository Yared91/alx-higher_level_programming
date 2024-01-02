#!/usr/bin/python3
"""Describes the text indentation function."""


def text_indentation(text):
    """Prints text with two new lines after each ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    a = 0
    while a < len(text) and text[a] == ' ':
        a = a + 1
    while a < len(text):
        print(text[a], end="")
        if text[a] == "\n" or text[a] in ".?:":
            if text[a] in ".?:":
                print("\n")
            a = a + 1
            while a < len(text) and text[a] == ' ':
                a = a + 1
            continue
        a = a + 1

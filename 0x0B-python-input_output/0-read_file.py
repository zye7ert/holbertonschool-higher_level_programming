#!/usr/bin/python3
""""
Write a function that reads a text file (UTF8)
and prints it to stdout:
"""


def read_file(filename=""):
    """function that reads a text"""
    with open("my_file_0.txt", encoding="utf8") as Myfile:
        print(Myfile.read())

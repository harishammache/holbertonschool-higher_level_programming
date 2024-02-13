#!/usr/bin/python3
"""
    class MyList that inherits from list
"""


class MyList(list):
    """prints the list, but sorted"""
    def __init__(self):
        pass

    def print_sorted(self):
        print(sorted(self))

#!/usr/bin/python3
"""Define a Square class."""


class Square:
    """Class Square with a size attribute."""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple) or len(value) != 2 or
            all(not isinstance(x, int) or x <= 0 for x in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print("")
            return
        if self.__position[1] > 0:
            print()
        else:
            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print('#' * self.__size)

    def area(self):
        return self.__size ** 2

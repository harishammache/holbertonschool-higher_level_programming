#!/usr/bin/python3
"""
    create an empty class
"""


class BaseGeometry:
    """
        Public instance method
    """

    def area(self):
        """method for calculated area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method for validate if a num is integer"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
        class Rectangle that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.__width = width
        self.integer_validator("width", self.__width)
        self.__height = height
        self.integer_validator("height", self.__height)

    def area(self):
        """the area() method must be implemented"""
        return self.__width * self.__height

    def __str__(self):
        """the following rectangle description"""
        return (f"[Rectangle] {self.__width}/{self.__height}")


class Square(Rectangle):
    """
        class square that inherits from rectangle.
    """

    def __init__(self, size):
        """Instantiation with size"""
        self.__size = size
        self.integer_validator("size", self.__size)

    def __str__(self):
        """
            Return the square description.
        """
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        """
            Method to calculate the area of the square.
        """
        return self.__size ** 2

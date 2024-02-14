#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
    create an empty class
"""


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

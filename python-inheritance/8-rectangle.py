#!/usr/bin/python3
"""
    create an empty class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        class Rectangle that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """Instantiation with width and height"""
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)
        self.__width = width
        self.__height = height

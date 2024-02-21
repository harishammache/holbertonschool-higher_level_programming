#!/usr/bin/python3
"""
    Write the class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """class rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print((" " * self.x) + ("#" * self.width))

    def update(self, *args, **kwargs):
        new_list = ['id', 'width', 'height', 'x', 'y']
        if args:
            for index, value in zip(new_list, args):
                setattr(self, index, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} -\
 {self.width}/{self.height}")

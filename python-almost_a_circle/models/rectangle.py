#!/usr/bin/python3
"""
    Write the class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """class rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """"Initialize Rectangle instance."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """"Getter method for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """"Setter method for width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter method for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Getter method for x-coordinate."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Setter method for x-coordinate."""
        return self.__x

    @x.setter
    def x(self, value):
        """Getter method for y-coordinate."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Getter method for y-coordinate."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y-coordinate."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Compute area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Display rectangle with '#' characters."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print((" " * self.x) + ("#" * self.width))

    def update(self, *args, **kwargs):
        """Update attributes of the rectangle."""
        new_list = ['id', 'width', 'height', 'x', 'y']
        if args:
            for index, value in zip(new_list, args):
                setattr(self, index, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Return string representation of the rectangle."""
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} -\
 {self.width}/{self.height}")

    def to_dictionary(self):
        """adding the public method"""
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}

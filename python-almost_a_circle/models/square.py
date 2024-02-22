#!/usr/bin/python3
"""
    Write the class Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """The overloading __str__ method """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.size)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ public method update"""
        attr = ["id", "size", "x", "y"]
        if len(args) > 0:
            for index, value in zip(attr, args):
                setattr(self, index, value)

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ public method"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

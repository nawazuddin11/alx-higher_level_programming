# models/rectangle.py

from models.base import Base

class Rectangle(Base):
    """Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # width
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__validate_integer("width", value)
        self.__validate_positive("width", value)
        self.__width = value

    # height
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__validate_integer("height", value)
        self.__validate_positive("height", value)
        self.__height = value

    # x
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__validate_integer("x", value)
        self.__validate_non_negative("x", value)
        self.__x = value

    # y
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__validate_integer("y", value)
        self.__validate_non_negative("y", value)
        self.__y = value

    # Validation methods
    def __validate_integer(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

    def __validate_positive(self, name, value):
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    def __validate_non_negative(self, name, value):
        if value < 0:
            raise ValueError(f"{name} must be >= 0")


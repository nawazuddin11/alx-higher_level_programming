#!/usr/bin/python3

"""Define a class Square."""


class Square:
     """Represent a square."""

    def __init__(self, size =0):

         """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        """ instantioating the size attribute """

        self.__size = size

    """ method to return the area of the square """

    def area(self):
        """Return the current area of the square."""

        return (self.__size * self.__size)



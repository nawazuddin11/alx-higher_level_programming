#!/usr/bin/python3


class Square:

    def __init__(self, size =0):

        """ checking for the instance of size """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        """ instantioating the size attribute """

        self.__size = size

    """ method to return the area of the square """

    def area(self):

        return self.__size * self.__size



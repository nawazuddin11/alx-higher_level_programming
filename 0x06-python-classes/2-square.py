#!/usr/bin/python3


"""this is a class with instnace size"""

class Square:

    def __init__(self,size =0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >=0")

        else:
            self.__size = size

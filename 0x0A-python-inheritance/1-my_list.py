#!/usr/bin/python3
""" sorts a list """

class Mylist(list):
    """

    A subclass of list with an additional method to print the list sorted in ascending order
    """

    def print_sorted(self):

        """
        print the list, but sorted in ascending order.
        Assume all elements are intiger
        """
        print(sorted(self)) 

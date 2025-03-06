#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    for l in range(x):
        try:
            print(l)

        except ValueError:
            pass

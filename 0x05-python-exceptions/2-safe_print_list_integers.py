#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    plist = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]))
        except (ValueError, TypeError):
            pass
        else:
            plist += 1
    print("")
    return (plist)

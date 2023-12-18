#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    plist = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            plist += 1
    except IndexError:
        pass
    print("")
    return (plist)

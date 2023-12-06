#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return 0
    total = sum(x[0] * x[1] for x in my_list)
    total_weight = sum(x[1] for x in my_list)
    return total / total_weight

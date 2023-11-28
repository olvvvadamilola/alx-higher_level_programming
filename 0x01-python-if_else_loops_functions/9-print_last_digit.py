def print_last_digit(number):
    lastnum = abs(number) % 10
    print("{}".format(lastnum), end="")
    return (lastnum)

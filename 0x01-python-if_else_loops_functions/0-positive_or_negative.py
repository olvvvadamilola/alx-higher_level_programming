#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if number > 0:
    print("{} is {}".format(number, "positive"))
elif number < 0:
    print("{} is {}".format(number, "negative"))
else:
    print("{} is {}".format(number, "zero"))

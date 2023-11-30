#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)

    c, operator, d = sys.argv[1:]

    if operator not in ['+', '-', '*', '/']:
        print(f"Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    c, d = map(int, (c, d))

    if operator == '+':
        result = add(c, d)
    elif operator == '-':
        result = sub(c, d)
    elif operator == '*':
        result = mul(c, d)
    elif operator == '/':
        if d == 0:
            print("Error: Division by zero")
            sys.exit(1)
        result = div(c, d)

    print("{} {} {} = {}".format(c, operator, d, result))

#!/usr/bin/python3

if __name__ == '__main__':

    from calculator_1 import add, sub, mul, div
    from sys import argv

    operators = ['+', '-', '*', '/']
    funcs = [add, sub, mul, div]
    result = 0

    if (len(argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if argv[2] not in operators:

        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:

        a = int(argv[1])
        b = int(argv[3])
        func = funcs[operators.index(argv[2])]
        op = argv[2]

        result = func(a, b)

        print("{} {} {} = {}".format(a, op, b, result))

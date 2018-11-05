#!/usr/bin/env python3

import operator
import readline
from termcolor import colored

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    'x': operator.xor
}


def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()


def main():
    while True:
        answer = calculate(input("rpn calc> "))

        if answer > 0:
            print(colored("Result: {}".format(answer), "blue"))

        elif answer == 0:
            print(colored("Result: {}".format(answer), "black"))

        else:
            print(colored("Result: {}".format(answer), "red"))


if __name__ == '__main__':
    main()

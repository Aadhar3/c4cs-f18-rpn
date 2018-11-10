#!/usr/bin/env python3

import operator
import readline
import math
from termcolor import colored

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    'x': operator.xor,
    '^': operator.pow,
    '//': operator.floordiv,
    'rs': operator.rshift
}


def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            if token.find('%') != -1:
                first = stack[0]
                token = token.replace('%', '')
                token = int(token)
                second = ((token/100)*first)
                stack.append(second)
            elif token == '!':
                first = stack[0]
                result = math.factorial(first)
                stack.pop()
                stack.append(result)
            else:
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
            print(colored("Result: {}".format(answer), "blue"))

        else:
            print(colored("Result: {}".format(answer), "red"))


if __name__ == '__main__':
    main()

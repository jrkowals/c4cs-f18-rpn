#!/usr/bin/env python3

def calculate(arg):
    stack = []

    tokens = arg.split()

    for token in tokens:
        try:
            stack.append(int(token))
        except ValueError:
            value1 = stack.pop()
            value2 = stack.pop()
            result = value1 + value2

            stack.append(result)
    return stack[0]

def main():
    while True:
        result = calculate(input('rpn calc> '))
        print(result)

if __name__ == '__main__':
    main()
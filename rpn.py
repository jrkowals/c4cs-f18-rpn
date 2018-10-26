#!/usr/bin/env python3

def calculate(arg):
    stack = []

    tokens = arg.split()

    for token in tokens:
        try:
            stack.append(int(token))
        except ValueError:
            value2 = stack.pop()
            value1 = stack.pop()
            if token == '+':
                result = value1 + value2
            elif token == '-':
                result = value1 - value2

            stack.append(result)
    if len(stack) > 1:
        raise ValueError('Stack size larger than one')
    
    return stack[0]

def main():
    while True:
        try:
            result = calculate(input('rpn calc> '))
            print(result)
        except ValueError:
            pass

if __name__ == '__main__':
    main()
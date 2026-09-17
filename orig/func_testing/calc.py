import sys
import math_lib

def main():
    op, x, y = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])

    if op == 'add':
        print(math_lib.add(x, y))
    elif op == 'sub':
        print(math_lib.sub(x, y))
    elif op == 'div':
        print(math_lib.div(x, y))
    else:
        print('unknown operation: ' + op + '\n')

if __name__ == '__main__':
    main()

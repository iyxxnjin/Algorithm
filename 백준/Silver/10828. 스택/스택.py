# stack
import sys
read = sys.stdin.readline

N = int(read())
stack = []

for _ in range(N):
    order = read().split()
    operation = order[0]
    num = order[1] if len(order) > 1 else None

    if operation == 'push':
        stack.append(num)

    elif operation == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif operation == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)

    elif operation == 'empty':
        if stack:
            print('0')
        else:
            print('1')

    elif operation == 'size':
        print(len(stack))


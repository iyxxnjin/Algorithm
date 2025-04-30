import sys
read = sys.stdin.readline

n = int(read())
stack = []
current = 1
result = []

for _ in range(n):
    num = int(read())

    while current <= num:
        stack.append(current)
        result.append('+')
        current += 1

    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        sys.exit()

print('\n'.join(result))

# stack
import sys
read = sys.stdin.readline

T = int(read())
for _ in range(T):
    PS = read().strip()
    stack = []
    for ch in PS:
        if ch == '(':
            stack.append(ch)
        else:
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")

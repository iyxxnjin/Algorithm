import sys
input = sys.stdin.readline

N, L = map(int, input().split())

for i in range(L, 101):
    x = N - i * (i - 1) // 2
    if x % i == 0:
        x = x // i
        if x >= 0:
            print(' '.join(map(str, range(x, x + i))))
            break
else:
    print(-1)

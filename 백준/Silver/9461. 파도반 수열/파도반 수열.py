import sys
input = sys.stdin.readline

P = [0] * 101
P[1] = P[2] = P[3] = 1
P[4] = P[5] = 2
P[6] = 3

for i in range(7, 101):
    P[i] = P[i-2] + P[i-3]

T = int(input())
for _ in range(T):
    N = int(input())
    print(P[N])

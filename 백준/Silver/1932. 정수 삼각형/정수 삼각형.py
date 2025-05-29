import sys
input = sys.stdin.readline

triangle = []
N = int(input())
for _ in range(N+1):
    M = list(map(int, input().split()))
    triangle.append(M)

for i in range(N-2, -1, -1):
    for j in range(len(triangle[i])):
        triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
    
print(triangle[0][0])
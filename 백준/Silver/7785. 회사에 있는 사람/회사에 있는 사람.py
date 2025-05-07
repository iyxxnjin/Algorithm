import sys
from collections import Counter

read = sys.stdin.readline

n = int(read())
names = [read().split()[0] for _ in range(n)]

count = Counter(names)
result = []

for name in count:
    if count[name] % 2 != 0:
        result.append(name)

for name in sorted(result, reverse=True):
    print(name)

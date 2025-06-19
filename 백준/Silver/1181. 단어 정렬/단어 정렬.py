import sys
input = sys.stdin.readline

N = int(input())
words = set()

for _ in range(N):
    word = input().strip()
    words.add(word)

list_words = list(words)
list_words.sort()
list_words.sort(key=len)  

for s in list_words:
    print(s)

import sys
input = sys.stdin.readline

N = int(input())

room = 1
num = 1

while N > num:
    num += 6 * room  
    room += 1
    
print(room)
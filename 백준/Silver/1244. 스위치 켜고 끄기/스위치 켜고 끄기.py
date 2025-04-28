import sys
read = sys.stdin.readline

n = int(read())
switches = list(map(int, read().split()))

def toggle_switch(switch_num):
    switches[switch_num] = 1 - switches[switch_num]

def check_symmetric(left, right):
    while left >= 0 and right < n:
        if switches[left] == switches[right]:
            toggle_switch(left)
            toggle_switch(right)
            left -= 1
            right += 1
        else:
            break

student = int(read())
for _ in range(student):
    sex, given_num = map(int, read().split())
    index = given_num - 1

    if sex == 1:
        for i in range(index, n, given_num):
            toggle_switch(i)
    else:
        toggle_switch(index)
        offset = 1

        left = index - offset
        right = index + offset
        check_symmetric(left, right)

for i in range(0, n, 20):
    print(" ".join(map(str, switches[i:i+20])))
def solution(l, r):
    answer = []

    for i in range(l, r + 1):
        is_valid = True
        for j in str(i):
            if j == '0' or j == '5':
                continue
            else:
                is_valid = False
                break
        if is_valid:
            answer.append(i)

    if not answer:
        return [-1]

    return answer

def solution(quiz):
    result = []
    for q in quiz:
        div_q = q.split()
             
        if div_q[1] == '-':
            answer = int(div_q[0]) - int(div_q[2])
        elif div_q[1] == '+':
            answer = int(div_q[0]) + int(div_q[2])

        if answer == int(div_q[4]):
            result.append("O")
        else:
            result.append("X")
    return result
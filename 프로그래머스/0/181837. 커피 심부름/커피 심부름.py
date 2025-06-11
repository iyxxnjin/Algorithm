def solution(order):
    cost = 0
    for i in order:
        if 'cafelatte' in i:
            cost += 5000
        else:
            cost += 4500
    return cost
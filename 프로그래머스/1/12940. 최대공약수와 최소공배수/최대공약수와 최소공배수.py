def solution(n, m):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    greatest = gcd(n, m)
    least = (n * m) // greatest

    answer = [greatest, least]
    return answer

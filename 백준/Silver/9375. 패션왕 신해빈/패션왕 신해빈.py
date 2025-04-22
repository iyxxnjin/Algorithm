tc = int(input())  # 테스트 케이스 수

for _ in range(tc):
    n = int(input())  # 의상 수
    
    # 의상 종류만 딕셔너리화
    clothes = {}

    for _ in range(n):
        name, kind = input().split()
        # 종류별 개수 세기
        if kind in clothes:
            clothes[kind] += 1
        else:
            clothes[kind] = 1

    # 모든 의상에(개수+1)를 곱하는 구조이므로 초기값을 1로 해야 결과값이 0이 되지 않음
    result = 1
    
    for count in clothes.values():
        result *= (count + 1)  # 안 입는 경우 포함

    print(result - 1)  # 아무것도 안 입은 경우 제외
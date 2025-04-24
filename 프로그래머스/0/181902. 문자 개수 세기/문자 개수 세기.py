# 입력: 문자열
# 52개 리스트 배열 생성
# 알파벳 대문자를 0-25 배열에, 소문자를 26-51에 담는다.
# my_string에서 해당하는 알파벳이 있으면 +1
# 결과값: list로 반환
def solution(my_string):
    # 52개 배열 생성
    answer = [0] * 52
    for i in my_string:
        if(ord(i) - ord('A')) <= 25:
            answer[ord(i) - ord('A')] += 1
        else:
            answer[ord(i) - ord('a') + 26] += 1
    return answer
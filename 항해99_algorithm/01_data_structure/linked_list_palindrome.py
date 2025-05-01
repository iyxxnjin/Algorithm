# ----------------------------------------
# 📌 회문 판별 알고리즘 (Palindrome Algorithm)
#
# 회문(palindrome): 앞뒤로 읽었을 때 동일한 문자열
# 단일 연결 리스트가 회문인지 판별하는 함수
#
# 🔍 동작 방식:
# 1. 연결 리스트가 비어 있으면 True 반환
# 2. 연결 리스트의 값을 배열에 저장
# 3. 배열의 앞뒤 값을 하나씩 꺼내 비교
#    - 값이 다르면 False
#    - 끝까지 같으면 True
#
# 🧠 시간복잡도:
#       - O(n^2) : list 사용 시 (arr.pop(0)은 O(n))
#       - O(n) : deque 사용 시 (dq.popleft는 O(1))
# 🧠 공간복잡도: O(n)
# ----------------------------------------

def isPalindrome(ln):
    arr = []
    head = ln.head

    if not head:
        return True

    node = head
    while node:
        arr.append(node.val)
        node = node.next

    while len(arr) > 1:
        first = arr.pop(0)
        last = arr.pop()
        if first != last:
            return False

    # while len(dq) > 1:
    #     if dq.popleft() != dq.pop():
    #         return False
    return True
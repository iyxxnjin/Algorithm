# ----------------------------------------
# 📌 스택 구현 알고리즘 (Stack Algorithm)
#
# 스택(stack): LIFO(Last In, First Out) 방식으로 데이터를 처리하는 자료구조
# 연결 리스트를 사용하여 스택을 구현한 클래스
#
# 🔍 동작 방식:
# 1. push(value): 스택에 값을 추가 (새로운 노드는 스택의 맨 위에 추가)
# 2. pop(): 스택에서 맨 위 값을 제거하고 반환
# 3. is_empty(): 스택이 비었는지 확인
#
# 🧠 시간복잡도:
#       - O(1): push, pop, is_empty 모두 상수 시간
# 🧠 공간복잡도: O(n)
# ----------------------------------------

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):
        if self.top is None:
            return None

        node = self.top
        self.top = self.top.next
        return node.val

    def is_empty(self):
        return self.top is None
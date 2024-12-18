from collections import deque

class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)  # 요소를 큐의 끝에 추가

    def pop(self) -> int:
        if not len(self.queue)==0:
            return self.queue.pop()  # 큐의 끝 요소를 제거하고 반환
        return None  # 빈 경우 None 반환 (필요 시 에러 처리)

    def top(self) -> int:
        if not self.empty():
            return self.queue[-1]  # 큐의 끝 요소를 반환
        return None  # 빈 경우 None 반환 (필요 시 에러 처리)

    def empty(self) -> bool:
        return len(self.queue) == 0  # 큐가 비어 있는지 확인

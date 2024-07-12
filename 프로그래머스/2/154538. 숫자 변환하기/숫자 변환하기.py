from collections import deque

def solution(x, y, n):
    if x == y:
        return 0
    
    queue = deque([(x, 0)])  # (현재 값, 연산 횟수)
    visited = set([x])  # 방문한 값들을 저장
    
    while queue:
        current, cnt = queue.popleft()
        
        for next_val in (current + n, current * 2, current * 3):
            if next_val == y:
                return cnt + 1
            if next_val < y and next_val not in visited:
                visited.add(next_val)
                queue.append((next_val, cnt + 1))
    
    return -1


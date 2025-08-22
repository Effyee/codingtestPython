from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    def one_diff(w1, w2):
        return sum(a!=b for a,b in zip(w1, w2)) == 1
    
    q = deque()
    q.append((begin, 0))
    visited = [False] * len(words)
    
    while q:
        now, cnt = q.popleft()
        if now == target:
            return cnt
        for i, word in enumerate(words):
            if not visited[i] and one_diff(now, word):
                visited[i] = True
                q.append((word, cnt+1))
    return 0

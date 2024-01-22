import sys
from collections import deque
n=int(sys.stdin.readline().strip())

def solution(n):
    q=deque([i for i in range(1,n+1)])
    while len(q)!=1:
        if q:
            q.popleft()
            q.append(q.popleft())
    print(q[0])

solution(n)
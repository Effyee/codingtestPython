import sys
from collections import deque
n=int(sys.stdin.readline())

l=deque([i for i in range(1,n+1)])

def solution(l):
    while len(l)!=1:
        if l:
            l.popleft()
            l.append(l.popleft())
        else:
            break
    print(l[0])

solution(l)

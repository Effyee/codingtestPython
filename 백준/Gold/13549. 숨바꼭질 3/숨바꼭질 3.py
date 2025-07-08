import sys
from collections import deque

input=sys.stdin.readline

n,k=map(int,input().split())
visited=[False]*(100001)

def bfs():
    q=deque()
    q.append((n,0))
    visited[n]=True
    while q:
        now,cnt=q.popleft()
        if now==k:
            print(cnt)
            break
        if 0<=2*now<100001 and not visited[2*now]:
            visited[2*now]=True
            q.append((2*now,cnt))
        for next in (now-1,now+1):
            if 0<=next<100001 and not visited[next]:
                visited[next]=True
                q.append((next,cnt+1))
    return

bfs()
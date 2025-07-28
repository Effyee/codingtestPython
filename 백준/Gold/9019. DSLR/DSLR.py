import sys
from collections import deque
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    number,target=map(int,input().split())
    q=deque()
    visited = [False] * 10000
    q.append((number,''))
    visited[number]=True
    while q:
        num,c=q.popleft()
        if num==target:
            print(c)
            break
        # D
        dn = (2*num) % 10000
        if not visited[dn]:
            visited[dn] = True
            q.append((dn,c+'D'))
        # S
        sn = num - 1 if num != 0 else 9999
        if not visited[sn]:
            visited[sn] = True
            q.append((sn,c+'S'))
        # L
        ln = (num % 1000) * 10 + num // 1000
        if not visited[ln]:
            visited[ln] = True
            q.append((ln,c+'L'))
        # R
        rn = (num % 10) * 1000 + num // 10
        if not visited[rn]:
            visited[rn] = True
            q.append((rn,c+'R'))

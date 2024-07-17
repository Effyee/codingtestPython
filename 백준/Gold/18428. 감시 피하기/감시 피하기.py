import sys
import copy
from collections import deque
from itertools import combinations
input=sys.stdin.readline

n=int(input())
graph=[]

for _ in range(n):
    graph.append(list(map(str,input().split())))

def bfs(graph):
    q=deque([(x,y) for x in range(n) for y in range(n) if graph[x][y]=='T'])

    while q:
        x,y=q.popleft()
        for dx,dy in zip([-1,1,0,0],[0,0,-1,1]):
            nx=x+dx
            ny=y+dy
            while 0<=nx<n and 0<=ny<n:
                if graph[nx][ny]=='S':
                    return False
                elif graph[nx][ny]=='O':
                    break
                else:
                    nx+=dx
                    ny+=dy
    return True

locations=[(x,y) for x in range(n) for y in range(n) if graph[x][y]=='X']

def solution():
    for c in combinations(locations,3):
        g=copy.deepcopy(graph)
        for x,y in c:
            g[x][y]='O'
        if bfs(g):
            return 'YES'
    return 'NO'

print(solution())


import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
village=[list(map(str,input().strip())) for _ in range(n)]
cost=[list(map(int,input().split())) for _ in range(n)]
flat=[cost[i][j] for i in range(n) for j in range(n)]
height=sorted(list(set(flat)))
# 배달 시작점
sx,sy=0,0
# 집의 갯수
vc=0

for i in range(n):
    for j in range(n):
        if village[i][j]=='P':
            sx,sy=i,j
        elif village[i][j]=='K':
            vc+=1

def bfs(l,r):
    if not(l <= (cost[sx][sy]) <= r):
        return False
    # 초기화
    dx=[0,0,-1,1,-1,1,-1,1]
    dy=[-1,1,0,0,-1,-1,1,1]
    visited=[[False]*n for _ in range(n)]
    q=deque()
    visited[sx][sy]=True
    q.append((sx,sy))
    count=0
    while q:
        x,y=q.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            # 방문 안한 칸일 때
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                # 범위 안에 들어오고
                if l<=(cost[nx][ny])<=r:
                    visited[nx][ny]=True
                    # 농지인 경우
                    if village[nx][ny]=='.':
                        q.append((nx,ny))
                    # 집인 경우
                    elif village[nx][ny]=='K':
                        count+=1
                        q.append((nx,ny))
    return count==vc

# 가장 작은 피로도 구하기
answer=int(1e9)
def solution():
    global answer
    left,right=0,0
    while left<len(height):
        while right<len(height):
            if bfs(height[left],height[right]):
                answer=min(answer,height[right]-height[left])
                break
            right+=1
        left+=1
    return

solution()
print(answer)
def hunt(archor):
    boards = deepcopy(board) # 보드 복사 
    visited = [[0] * M for _ in range(N)] # 방문처리
    cnt = 0
    for i in range(N-1, -1, -1): # 한칸씩 전진(적이 아닌 궁수가 전진) (조건5)
        die = []
        for m in archor: # 뽑은 궁수 자리에 대해 (조건2)
            queue = deque([[i, m, 1]])
            while queue:
                y, x, d = queue.popleft()
                if boards[y][x] :
                    die.append([y, x])
                    if not visited[y][x]:
                        visited[y][x] = 1
                        cnt += 1 # 죽였으니 점수 증가
                    break

                if d < D: # 사정거리보다 짧으면 (조건4)
                    for dx, dy in move:
                        nx, ny = x + dx, y + dy
                        if 0 <= ny < N and 0 <= nx < M:
                            queue.append([ny, nx, d+1]) # 거리 증가

        for y, x in die:# (조건3) 모든 궁수가 동시에 공격하니 마지막에 처리
            boards[y][x] = 0

    return cnt

import sys
from copy import deepcopy
from collections import deque
from itertools import combinations
N, M, D = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # (조건 1)
move = [[-1,0],[0,-1],[1,0]]
result = 0
for archor in combinations([i for i in range(M)], 3): #(조건2)
    result = max(result, hunt(archor))
print(result)
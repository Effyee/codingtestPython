import sys
import copy
input = sys.stdin.readline

graph = []
for _ in range(4):
    a1,b1,a2,b2,a3,b3,a4,b4 = map(int, input().split())
    graph.append([(a1,b1), (a2,b2), (a3,b3), (a4,b4)])

# 방향: 0(dummy), ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0,  0, -1, -1, -1, 0, 1, 1, 1]

def move_fish(graph):
    for fish_num in range(1, 17):
        found = False
        for x in range(4):
            for y in range(4):
                if graph[x][y][0] == fish_num:
                    dir = graph[x][y][1]
                    for _ in range(8):
                        nx = x + dx[dir]
                        ny = y + dy[dir]
                        if 0 <= nx < 4 and 0 <= ny < 4 and graph[nx][ny][0] != 17:
                            # 방향 업데이트 후 swap
                            graph[x][y] = (fish_num, dir)
                            graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
                            break
                        dir = (dir % 8) + 1
                    found = True
                    break
            if found:
                break
    return graph

answer = 0

def bt(x, y, dir, score, graph):
    global answer
    answer = max(answer, score)

    g = copy.deepcopy(graph)
    g = move_fish(g)

    #moved = False
    for i in range(1, 4):
        nx = x + dx[dir]*i
        ny = y + dy[dir]*i
        if 0 <= nx < 4 and 0 <= ny < 4 and g[nx][ny][0] != 0:
            #moved = True
            fish_num, new_dir = g[nx][ny]
            prev_val = g[x][y]
            g[x][y] = (0, 0)
            g[nx][ny] = (17, new_dir)
            bt(nx, ny, new_dir, score + fish_num, g)
            g[nx][ny] = (fish_num, new_dir)
            g[x][y] = prev_val
    return

# 상어가 (0,0) 물고기 먹고 시작
start_fish, start_dir = graph[0][0]
graph[0][0] = (17, start_dir)
bt(0, 0, start_dir, start_fish, graph)
print(answer)

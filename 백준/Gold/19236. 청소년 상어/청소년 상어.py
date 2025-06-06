import sys
import copy

input = sys.stdin.readline

graph = []
for _ in range(4):
    a1, b1, a2, b2, a3, b3, a4, b4 = map(int, input().split())
    graph.append([(a1, b1), (a2, b2), (a3, b3), (a4, b4)])

dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]


def fish_move(g):
    current_fish = 1
    while current_fish <= 16:
        found = False
        for i in range(4):
            for j in range(4):
                if g[i][j][0] == current_fish:
                    x, y = i, j
                    dir = g[i][j][1]
                    found = True
                    break
            if found:
                break
        if not found:
            current_fish += 1
            continue

        for _ in range(8):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < 4 and 0 <= ny < 4 and g[nx][ny][0] != 17:
                g[x][y] = (current_fish, dir)
                g[x][y], g[nx][ny] = g[nx][ny], g[x][y]
                break
            dir = dir % 8 + 1
        current_fish += 1
    return g


answer = -int(1e9)


def bt(x, y, dir, score, graph):
    global answer

    moved = False
    for step in range(1, 4):  # 최대 3칸 이동으로 수정
        nx = x + dx[dir] * step
        ny = y + dy[dir] * step
        if 0 <= nx < 4 and 0 <= ny < 4 and 1 <= graph[nx][ny][0] <= 16:
            moved = True
            new_graph = copy.deepcopy(graph)
            fish_num, new_dir = new_graph[nx][ny]
            new_score = score + fish_num
            new_graph[nx][ny] = (17, new_dir)
            new_graph[x][y] = (0, 0)
            fish_move(new_graph)  # 물고기 이동 후 재귀 호출
            bt(nx, ny, new_dir, new_score, new_graph)

    if not moved:
        answer = max(answer, score)


# 초기 상어 위치 및 물고기 이동 처리
start_fish = graph[0][0]
graph[0][0] = (17, start_fish[1])
fish_move(graph)  # 첫 물고기 이동 수행
bt(0, 0, start_fish[1], start_fish[0], graph)  # 초기 점수 설정

print(answer)

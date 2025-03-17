import sys

input = sys.stdin.readline

N = int(input())
students = {}

for _ in range(N * N):
    a, b, c, d, e = map(int, input().split())
    students[a] = {b, c, d, e}  # 좋아하는 학생들을 집합으로 저장

graph = [[0] * N for _ in range(N)]


# 조건 1: 인접한 칸에 좋아하는 학생이 가장 많은 칸을 찾는 함수
def check(x, y, student):
    total = 0
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] in students[student]:  # 좋아하는 학생이 주변에 있는지 확인
                total += 1
    return total, x, y


# 조건 2: 비어있는 칸이 가장 많은 곳 찾기
def check_space(x, y):
    total = 0
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0:
            total += 1
    return total, x, y


# 학생 배치
for student in students.keys():  # 학생 번호 순서대로 배치
    candidates = []
    max_friends = -1

    for x in range(N):
        for y in range(N):
            if graph[x][y] == 0:  # 빈 칸만 확인
                friends, _, _ = check(x, y, student)

                if friends > max_friends:
                    max_friends = friends
                    candidates = [(x, y)]
                elif friends == max_friends:
                    candidates.append((x, y))

    # 좋아하는 친구가 가장 많은 칸이 하나라면 배치
    if len(candidates) == 1:
        x, y = candidates[0]
        graph[x][y] = student
        continue

    # 조건 2 적용: 비어있는 칸이 가장 많은 곳 찾기
    spaces = []
    max_spaces = -1
    for x, y in candidates:
        empty_count, _, _ = check_space(x, y)

        if empty_count > max_spaces:
            max_spaces = empty_count
            spaces = [(x, y)]
        elif empty_count == max_spaces:
            spaces.append((x, y))

    # 최종 배치
    x, y = sorted(spaces)[0]  # 행, 열 기준으로 정렬하여 가장 작은 위치 선택
    graph[x][y] = student

# 만족도 계산
satisfaction = 0
score_map = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}

for x in range(N):
    for y in range(N):
        student = graph[x][y]
        friends, _, _ = check(x, y, student)
        satisfaction += score_map[friends]

print(satisfaction)

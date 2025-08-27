import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())

# 상어 정보 저장: (r, c, s, d, z)
sharks = []
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks.append((r-1, c-1, s, d, z))  # 0-index로 변환

answer = 0
# 방향 벡터 (1: 위, 2: 아래, 3: 오른쪽, 4: 왼쪽)
dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, 1, -1]

# 낚시꾼이 왼쪽→오른쪽으로 이동
for fisher in range(C):
    # 1. 상어 잡기 (해당 열에서 가장 위에 있는 상어)
    sharks.sort(key=lambda x: (x[1], x[0]))  # 열→행 순으로 정렬
    for i, (r, c, s, d, z) in enumerate(sharks):
        if c == fisher:   # 현재 열에 상어가 있으면
            answer += z   # 크기 더하고
            sharks.pop(i) # 잡아서 제거
            break

    # 2. 상어 이동
    new_shark = {}
    for r, c, s, d, z in sharks:
        # 속력 줄이기 
        if d in (1, 2):  # 위/아래
            s %= (R - 1) * 2
        else:  # 왼/오
            s %= (C - 1) * 2

        # s번 이동
        for _ in range(s):
            nr, nc = r + dr[d], c + dc[d]
            if nr < 0 or nr >= R or nc < 0 or nc >= C:  # 벽 만나면
                if d == 1: d = 2
                elif d == 2: d = 1
                elif d == 3: d = 4
                elif d == 4: d = 3
                nr, nc = r + dr[d], c + dc[d]
            r, c = nr, nc

        # 같은 칸에 상어 있으면 크기 큰 상어만 남김
        if (r, c) not in new_shark or new_shark[(r, c)][4] < z:
            new_shark[(r, c)] = (r, c, s, d, z)

    # 상어 갱신
    sharks = list(new_shark.values())

print(answer)

import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())

sharks = []
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks.append((r-1, c-1, s, d, z))  # 0-index

answer = 0

for fisher in range(C):
    # 1. 상어 잡기
    sharks.sort(key=lambda x: (x[1], x[0]))  # 열 → 행
    for i, (r, c, s, d, z) in enumerate(sharks):
        if c == fisher:
            answer += z
            sharks.pop(i)
            break

    # 2. 상어 이동
    new_shark = {}
    for r, c, s, d, z in sharks:
        if d in (1, 2):  # 위/아래
            move = s % ((R - 1) * 2)
            pos = (r + (move if d == 2 else -move)) % ((R - 1) * 2)
            if pos >= R:  # 반사
                r = (R - 1) - (pos - (R - 1))
                d = 1 if d == 2 else 2
            else:
                r = pos
        else:  # 왼/오
            move = s % ((C - 1) * 2)
            pos = (c + (move if d == 3 else -move)) % ((C - 1) * 2)
            if pos >= C:
                c = (C - 1) - (pos - (C - 1))
                d = 4 if d == 3 else 3
            else:
                c = pos

        # 충돌 시 크기 큰 상어만 남기기
        if (r, c) not in new_shark or new_shark[(r, c)][4] < z:
            new_shark[(r, c)] = (r, c, s, d, z)

    sharks = list(new_shark.values())

print(answer)

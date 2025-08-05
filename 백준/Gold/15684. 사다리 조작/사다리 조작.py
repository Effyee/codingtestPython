import sys
input=sys.stdin.readline

n, m, h = map(int, input().split())
ladder = [[0] * (n + 2) for _ in range(h + 2)]  # n+2로 범위 초과 방지

for _ in range(m):
    a, b = map(int, input().split())
    ladder[a][b] = 1

def check():
    for i in range(1, n+1):
        x, y = 1, i  # i번 세로선에서 시작
        while x <= h:
            if y < n and ladder[x][y] == 1:
                y += 1
            elif y > 1 and ladder[x][y-1] == 1:
                y -= 1
            x += 1
        if y != i:
            return False
    return True

answer = 4

def backtrack(idx, x, y):
    global answer
    if check():
        answer = min(answer, idx)
        return
    if idx == 3:
        return

    for i in range(x, h + 1):
        k = y if i == x else 1
        for j in range(k, n):
            if j + 1 > n:  # 오른쪽으로 놓을 수 없음
                continue
            if ladder[i][j] == 1 or ladder[i][j - 1] == 1 or ladder[i][j + 1] == 1:
                continue

            ladder[i][j] = 1
            backtrack(idx + 1, i, j)
            ladder[i][j] = 0

backtrack(0, 1, 1)
print(answer if answer < 4 else -1)
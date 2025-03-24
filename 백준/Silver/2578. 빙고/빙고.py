import sys
input = sys.stdin.readline

bingo = [list(map(int, input().split())) for _ in range(5)]
l = []
for _ in range(5):
    l += list(map(int, input().split()))

visited = [[0]*5 for _ in range(5)]

def check():
    cnt = 0
    # 행 검사
    for i in range(5):
        if sum(visited[i]) == 5:
            cnt += 1
    # 열 검사 (수정 포인트!)
    for i in range(5):
        col = 0
        for j in range(5):
            col += visited[j][i]
        if col == 5:
            cnt += 1
    # 대각선 검사
    a = 0
    for i in range(5):
        a += visited[i][i]
    if a == 5:
        cnt += 1
    b = 0
    for i in range(5):
        b += visited[i][4 - i]
    if b == 5:
        cnt += 1
    return cnt >= 3

cnt = 0
for number in l:
    for x in range(5):
        for y in range(5):
            if bingo[x][y] == number:
                visited[x][y] = 1
                cnt += 1
                if check():
                    print(cnt)
                    exit()

import sys
input = sys.stdin.readline

bingo = []
visited = [[0] * 5 for _ in range(5)]  # 방문 체크 배열

# 5x5 빙고판 입력
for _ in range(5):
    bingo.append(list(map(int, input().split())))

# 사회자가 부른 숫자 입력
numbers = []
for _ in range(5):  # 5줄 입력받기
    numbers += list(map(int, input().split()))

# 빙고 개수를 세는 함수
def count_bingo():
    count = 0  # 빙고 개수

    # 가로 빙고 체크
    for row in visited:
        if sum(row) == 5:
            count += 1

    # 세로 빙고 체크
    for col in range(5):
        if sum(visited[row][col] for row in range(5)) == 5:
            count += 1

    # 대각선 빙고 체크
    if sum(visited[i][i] for i in range(5)) == 5:  # 좌상단 → 우하단
        count += 1
    if sum(visited[i][4 - i] for i in range(5)) == 5:  # 우상단 → 좌하단
        count += 1

    return count

# 사회자가 부른 숫자를 하나씩 지우면서 진행
for i, num in enumerate(numbers):
    for x in range(5):
        for y in range(5):
            if bingo[x][y] == num:
                visited[x][y] = 1  # 숫자 체크

                # 빙고 개수가 3개 이상이면 즉시 종료
                if count_bingo() >= 3:
                    print(i + 1)
                    exit()

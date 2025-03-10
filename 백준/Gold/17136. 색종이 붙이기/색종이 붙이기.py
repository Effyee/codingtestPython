import sys

input = sys.stdin.readline

# 10x10 종이판
graph = [list(map(int, input().split())) for _ in range(10)]
# 색종이 개수 (각 크기별 최대 5개)
paper_count = {size: 5 for size in range(1, 6)}
# 최소 색종이 개수 초기화
min_count = float('inf')

def can_attach(x, y, size):
    """x, y 위치에서 size 크기의 색종이를 붙일 수 있는지 확인"""
    if x + size > 10 or y + size > 10:  # 경계를 벗어나면 불가능
        return False
    for i in range(size):
        for j in range(size):
            if graph[x + i][y + j] == 0:  # 1이 아닌 곳이 있으면 불가능
                return False
    return True

def attach(x, y, size, value):
    """x, y 위치에 size 크기의 색종이를 붙이거나 제거"""
    for i in range(size):
        for j in range(size):
            graph[x + i][y + j] = value  # 0이면 색종이 제거, 1이면 붙임

def backtrack(count):
    """백트래킹을 이용한 최소 색종이 개수 탐색"""
    global min_count

    # 현재 count가 최소 개수보다 크면 더 볼 필요 없음 (가지치기)
    if count >= min_count:
        return

    # 덮을 1이 남아 있는지 확인
    for x in range(10):
        for y in range(10):
            if graph[x][y] == 1:
                # 가능한 모든 색종이 크기 (5x5부터 1x1까지)
                for size in range(5, 0, -1):
                    if paper_count[size] > 0 and can_attach(x, y, size):
                        # 색종이 붙이기
                        attach(x, y, size, 0)
                        paper_count[size] -= 1

                        # 다음 단계 백트래킹
                        backtrack(count + 1)

                        # 원상 복구 (백트래킹)
                        attach(x, y, size, 1)
                        paper_count[size] += 1
                return  # 여기서 return 해야 다른 경우를 탐색하지 않음

    # 모든 1을 덮었다면 최소 색종이 개수 갱신
    min_count = min(min_count, count)

# 백트래킹 시작
backtrack(0)

# 결과 출력
print(min_count if min_count != float('inf') else -1)

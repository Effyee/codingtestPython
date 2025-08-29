import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

wp, bp = 0, 0  # 흰색, 파란색 색종이 개수

def merge_sort(row, col, length):
    global wp, bp

    # 기준 색깔
    standard = paper[row][col]
    flag = True

    # 영역 전체가 같은 색인지 확인
    for i in range(row, row + length):
        for j in range(col, col + length):
            if paper[i][j] != standard:
                flag = False
                break
        if not flag:
            break

    # 모두 같은 색이면 카운트
    if flag:
        if standard == 0:
            wp += 1
        else:
            bp += 1
        return

    # 4분할
    half = length // 2
    merge_sort(row, col, half)                 # 좌상단
    merge_sort(row, col + half, half)          # 우상단
    merge_sort(row + half, col, half)          # 좌하단
    merge_sort(row + half, col + half, half)   # 우하단

# 전체 영역 호출
merge_sort(0, 0, n)
print(wp)
print(bp)

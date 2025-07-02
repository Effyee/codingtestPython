import sys
input = sys.stdin.readline

def right(arr, n):
    new_arr = [row[:] for row in arr]
    mid = n // 2
    for i in range(n):
        new_arr[i][mid] = arr[i][i]
        new_arr[i][n - 1 - i] = arr[i][mid]
        new_arr[mid][i] = arr[n - 1 - i][i]
        new_arr[i][i] = arr[mid][i]
    return new_arr

def left(arr, n):
    new_arr = [row[:] for row in arr]
    mid = n // 2
    for i in range(n):
        new_arr[i][i] = arr[i][mid]
        new_arr[mid][i] = arr[i][i]
        new_arr[n - 1 - i][i] = arr[mid][i]
        new_arr[i][mid] = arr[i][n - 1 - i]
    return new_arr

t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    time = abs(d) // 45
    for _ in range(time):
        if d < 0:
            arr = left(arr, n)
        else:
            arr = right(arr, n)

    for row in arr:
        print(*row)

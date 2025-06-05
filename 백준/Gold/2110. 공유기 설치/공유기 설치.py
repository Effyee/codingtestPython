import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = sorted(int(input()) for _ in range(n))

def bs():
    start, end = 1, arr[-1] - arr[0]
    answer = 0
    while start <= end:
        mid = (start + end) // 2

        cnt = 1
        last = arr[0]
        for i in range(1, n):
            if arr[i] - last >= mid:
                cnt += 1
                last = arr[i]

        if cnt >= c:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

    return answer

print(bs())
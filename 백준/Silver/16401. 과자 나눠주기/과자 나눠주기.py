import sys
input = sys.stdin.readline

m, n = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def bs():
    start, end = 1, arr[-1] 
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        r = sum(a // mid for a in arr)
        if r >= m:
            answer = mid  # 조건 만족, 더 큰 값 탐색
            start = mid + 1
        else:
            end = mid - 1
    return answer

print(bs())

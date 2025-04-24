import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
money = int(input())

def binary_search():
    start, end = 0, max(arr)
    result = 0

    while start <= end:
        mid = (start + end) // 2
        total = sum(min(x, mid) for x in arr)

        if total <= money:
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    return result

print(binary_search())

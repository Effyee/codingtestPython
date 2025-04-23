import sys
input = sys.stdin.readline

def lower_bound(arr, x):
    start, end = 0, len(arr)
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < x:
            start = mid + 1
        else:
            end = mid
    return start

def upper_bound(arr, x):
    start, end = 0, len(arr)
    while start < end:
        mid = (start + end) // 2
        if arr[mid] <= x:
            start = mid + 1
        else:
            end = mid
    return start

n = int(input())
cards = list(map(int, input().split()))
cards.sort()

m = int(input())
queries = list(map(int, input().split()))

result = []
for x in queries:
    low = lower_bound(cards, x)
    high = upper_bound(cards, x)
    result.append(str(high - low))

print(' '.join(result))

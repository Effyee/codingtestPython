import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
nums = list(map(int, input().split()))


# target 이상인 인덱스 중 가장 작은 (없으면 -1)
def lower_bound(target):
    answer = -1
    start, end = 0, n - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] >= target:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    return answer

# target 초과인 인덱스 중 가장 작은 (없으면 -1)
def upper_bound(target):
    answer = -1
    start, end = 0, n - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] > target:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    return answer

result = []
for num in nums:
    low = lower_bound(num)
    up = upper_bound(num)

    # 없는 경우
    if low == -1:
        result.append(0)
    else:
        if up == -1:  # num보다 큰 값이 없으면 → 끝까지 다 num임
            up = n
        result.append(up - low)

print(" ".join(map(str, result)))

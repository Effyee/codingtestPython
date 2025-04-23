import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))

start, end = 0, 0
count = 0
answer = 0

while end < n:
    if nums[end] % 2 == 1:
        count += 1

    while count > k:
        if nums[start] % 2 == 1:
            count -= 1
        start += 1

    answer = max(answer, end - start + 1 - count)
    end += 1

print(answer)

n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 처음 k개의 합으로 시작
re = sum(arr[:k])
answer = re

for i in range(k, n):
    re = re - arr[i - k] + arr[i]
    answer = max(answer, re)

print(answer)

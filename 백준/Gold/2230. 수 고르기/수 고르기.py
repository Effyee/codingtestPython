import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

left = 0
right = 0
INF = 10**18
answer = INF

while left < n and right < n:
    diff = arr[right] - arr[left]
    if diff < m:
        right += 1
    else:
        if diff < answer:
            answer = diff
        left += 1

        if left == right:
            right += 1

print(answer)

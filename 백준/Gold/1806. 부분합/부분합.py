import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 0
current = 0
INF = 10**9
answer = INF

while True:
    if current >= s:
        answer = min(answer, right - left)
        current -= arr[left]
        left += 1
    else:
        if right == n:
            break
        current += arr[right]
        right += 1

print(0 if answer == INF else answer)

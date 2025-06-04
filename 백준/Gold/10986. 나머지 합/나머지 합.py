import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

pre = [0] * (n + 1)
count = [0] * m
answer = 0

for i in range(n):
    pre[i + 1] = pre[i] + arr[i]
    r = pre[i + 1] % m
    count[r] += 1
    if r == 0:
        answer += 1 

for c in count:
    if c >= 2:
        answer += c * (c - 1) // 2

print(answer)
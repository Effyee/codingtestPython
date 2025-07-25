import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

re = 0
start, end = 0, 0
answer = int(1e9)

while end <= n: 
    if re < s:
        if end == n:  
            break
        re += arr[end]
        end += 1
    elif re >= s:
        answer = min(answer, end - start)
        re -= arr[start]
        start += 1

print(0 if answer == int(1e9) else answer)

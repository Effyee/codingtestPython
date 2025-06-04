import sys
input = sys.stdin.readline

n = int(input())
start, end = 1, 1
re = 1
answer = 0

while start <= n:
    if re < n:
        end += 1
        re += end
    elif re > n:
        re -= start
        start += 1
    else:  # re == n
        answer += 1
        re -= start
        start += 1

print(answer)
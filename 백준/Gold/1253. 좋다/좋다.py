import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

answer = 0
for i in range(n):
    now = arr[i]
    start, end = 0, n - 1

    while start < end:
        if start == i:
            start += 1
            continue
        if end == i:
            end -= 1
            continue

        total = arr[start] + arr[end]

        if total == now:
            answer += 1
            break  
        elif total < now:
            start += 1
        else:  
            end -= 1

print(answer)
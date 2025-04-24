import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
x = list(map(int, input().split()))

def is_possible(height):
    left = 0
    for light in x:
        if light - height > left:
            return False
        left = light + height
    return left >= n

start, end = 0, n
answer = n

while start <= end:
    mid = (start + end) // 2
    if is_possible(mid):
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)
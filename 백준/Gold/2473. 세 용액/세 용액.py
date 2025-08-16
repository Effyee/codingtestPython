import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().strip().split()))
arr.sort()
ans = [0, 0, 0]
res = float('inf')

for i in range(N-2):
    l, r = i+1, N-1
    while l < r:
        curr = arr[i] + arr[l] + arr[r]
        if abs(curr) < abs(res):
            ans = [arr[i], arr[l], arr[r]]
            res = curr
        if curr > 0:
            r -= 1
        elif curr < 0:
            l += 1
        else:   # curr == 0
            print(arr[i], arr[l], arr[r])
            sys.exit()
for num in ans:
    print(num, end=' ')
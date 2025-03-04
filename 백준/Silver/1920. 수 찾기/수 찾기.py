import sys
input = sys.stdin.readline

N = int(input())
nl = list(map(int, input().split()))
nl.sort()  

M = int(input())
ml = list(map(int, input().split()))

def bs(start, end, num):
    while start <= end:
        mid = (start + end) // 2
        if nl[mid] == num:
            return 1
        elif nl[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for num in ml:
    print(bs(0, N - 1, num))  

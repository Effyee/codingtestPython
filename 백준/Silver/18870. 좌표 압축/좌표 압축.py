import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

sorted_arr = sorted(set(arr))

result = [str(bisect_left(sorted_arr, x)) for x in arr]

print(' '.join(result))

import sys
from bisect import bisect_left
from collections import Counter

input = sys.stdin.readline

M, N = map(int, input().split())
universes = [list(map(int, input().split())) for _ in range(M)]

patterns = []

for universe in universes:
    sorted_uni = sorted(set(universe))
    compressed = tuple(bisect_left(sorted_uni, x) for x in universe)
    patterns.append(compressed)

count = 0
counter = Counter(patterns)

for freq in counter.values():
    if freq > 1:
        count += freq * (freq - 1) // 2

print(count)
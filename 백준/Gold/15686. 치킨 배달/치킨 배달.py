from itertools import combinations
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

houses = [(x, y) for x in range(n) for y in range(n) if city[x][y] == 1]
chickens = [(x, y) for x in range(n) for y in range(n) if city[x][y] == 2]

answer = int(1e9)

for comb in combinations(chickens, m):
    total = 0
    for hx, hy in houses:
        dist = int(1e9)
        for cx, cy in comb:
            dist = min(dist, abs(hx - cx) + abs(hy - cy))
        total += dist
    answer = min(answer, total)

print(answer)

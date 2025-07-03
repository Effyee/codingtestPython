import math
import sys
from itertools import combinations

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    coords = [list(map(int, input().split())) for _ in range(n)]

    total_x = sum(x for x, y in coords)
    total_y = sum(y for x, y in coords)

    result = math.inf

    half = len(list(combinations(coords, n // 2))) // 2
    for comb in list(combinations(coords, n // 2))[:half]:
        sum_x = sum(x for x, y in comb)
        sum_y = sum(y for x, y in comb)

        # 나머지 반은 전체 합에서 빼면 됨
        dx = total_x - 2 * sum_x
        dy = total_y - 2 * sum_y

        dist = math.sqrt(dx ** 2 + dy ** 2)
        result = min(result, dist)

    print(f"{result:.12f}")

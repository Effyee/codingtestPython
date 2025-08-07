import sys
import heapq
input=sys.stdin.readline

N, K = map(int, input().split())
jewels = []
for _ in range(N):
    m, v = map(int, input().split())
    jewels.append((m, v))

bags = [int(input()) for _ in range(K)]

jewels.sort(key=lambda x: x[0])
bags.sort()

max_heap = []
result = 0
j = 0 

for bag in bags:
    while j < N and jewels[j][0] <= bag:
        heapq.heappush(max_heap, -jewels[j][1])
        j += 1

    if max_heap:
        result += -heapq.heappop(max_heap)

print(result)

import sys
import heapq
input = sys.stdin.readline

n = int(input())
classes = [list(map(int, input().split())) for _ in range(n)]

classes.sort()

hq = []
heapq.heappush(hq, classes[0][1])

for i in range(1, n):
    start, end = classes[i]

    # 가장 빨리 끝나는 수업이 현재 수업보다 먼저 끝났으면, 그 강의실 재사용
    if hq[0] <= start:
        heapq.heappop(hq)

    heapq.heappush(hq, end)

print(len(hq))
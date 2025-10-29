import sys
import heapq
input = sys.stdin.readline

n = int(input())
classes = []
for _ in range(n):
    start, end = map(int, input().split())
    classes.append((start, end))

classes.sort()  
hq = []
answer = 0

for start, end in classes:
    # 가장 빨리 끝나는 강의실이 현재 수업 시작 전에 끝났으면 재활용
    if hq and hq[0] <= start:
        heapq.heappop(hq)
    heapq.heappush(hq, end)
    answer = max(answer, len(hq))

print(answer)

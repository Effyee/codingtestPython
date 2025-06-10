import sys
from collections import deque
input = sys.stdin.readline

graph = [deque(map(int, input().strip())) for _ in range(4)]

def left(num, dir):
    if num - 1 >= 0:
        if graph[num - 1][2] != graph[num][6]:
            left(num - 1, -dir)
            graph[num - 1].rotate(-dir)

def right(num, dir):
    if num + 1 < 4:
        if graph[num][2] != graph[num + 1][6]:
            right(num + 1, -dir)
            graph[num + 1].rotate(-dir)

k = int(input())
for _ in range(k):
    num, dir = map(int, input().split())
    num -= 1
    left(num, dir)
    right(num, dir)
    graph[num].rotate(dir)

answer = 0
for i in range(4):
    if graph[i][0] == 1:
        answer += (1 << i)
print(answer)
import sys
from collections import deque

def solution(command, queue):
    if command[0]=='push':
        queue.append(int(command[1]))
    elif command[0]=='pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif command[0]=='size':
        print(len(queue))
    elif command[0]=='empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif command[0]=='front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    else:  
        if queue:
            print(queue[-1])
        else:
            print(-1)

n=int(sys.stdin.readline().rstrip())
queue = deque()
for _ in range(n):
    command=sys.stdin.readline().rstrip().split()
    solution(command, queue)

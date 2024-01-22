import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque()

for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push_front':
        q.appendleft(int(command[1]))
    elif command[0] == 'push_back':
        q.append(int(command[1]))
    elif command[0] == 'pop_front':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if q:
            print(q.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == 'empty':
        print(0 if q else 1)
    elif command[0] == 'front':
        print(q[0] if q else -1)
    elif command[0] == 'back':
        print(q[-1] if q else -1)

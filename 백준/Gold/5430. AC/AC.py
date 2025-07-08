import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    p = input().strip()
    n = int(input())
    a = eval(input().strip())
    q = deque(a)

    rev = False
    error_flag = False

    for cmd in p:
        if cmd == 'R':
            rev = not rev  # reverse 대신 플래그로 처리
        else:
            if q:
                if rev:
                    q.pop()
                else:
                    q.popleft()
            else:
                print('error')
                error_flag = True
                break

    if not error_flag:
        if rev:
            q.reverse()
        print('[' + ','.join(map(str, q)) + ']')

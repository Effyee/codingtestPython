from collections import deque
import sys


def josephus(n, k):
    dq = deque(range(1, n + 1))
    result = []

    while dq:
        dq.rotate(-k + 1)  # rotate the deque k-1 to the left
        result.append(dq.popleft())  # remove the kth person

    return "<" + ", ".join(map(str, result)) + ">"


n, k = map(int, sys.stdin.readline().split())
print(josephus(n, k))

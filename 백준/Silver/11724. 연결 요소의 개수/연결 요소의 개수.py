import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])  
    return parent[x]

def make_union(a, b, parent):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(N + 1)]

for _ in range(M):
    start, end = map(int, input().split())
    make_union(start, end, parent)

for i in range(1, N+1):
    find_parent(parent, i)

print(len(set(parent[1:]))) 
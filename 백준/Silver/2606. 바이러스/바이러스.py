import sys
input = sys.stdin.readline

n = int(input())
pairs = int(input())

def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]

def make_union(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(n+1)]

for _ in range(pairs):
    a, b = map(int, input().split())
    make_union(a, b, parent)

answer = 0
for i in range(2, n+1):
    if find_parent(i, parent) == find_parent(1, parent):
        answer += 1

print(answer)

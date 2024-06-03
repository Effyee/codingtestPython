def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def make_union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, computers):
    parent = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                make_union(parent, i, j)

    # 모든 노드에 대해 최종 부모를 찾는 과정
    for i in range(n):
        find_parent(parent, i)

    # 최종 부모의 개수를 세어 네트워크의 개수를 계산
    return len(set(parent))


def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]

def make_union(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)

    if a != b:  # a와 b가 다르면 union
        parent[b] = a

def solution(n, computers):
    parent = [i for i in range(n)]  # 부모 배열 초기화

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                make_union(i, j, parent)

    # 네트워크의 개수 세기
    network_count = len(set(find_parent(i, parent) for i in range(n)))
    return network_count
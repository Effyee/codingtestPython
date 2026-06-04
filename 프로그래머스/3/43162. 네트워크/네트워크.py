def solution(n, computers):
    parent = [i for i in range(n)]

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

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                make_union(i, j, parent)

    for i in range(n):
        parent[i] = find_parent(i, parent)

    return len(set(parent))
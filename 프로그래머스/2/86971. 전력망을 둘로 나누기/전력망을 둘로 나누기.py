from itertools import combinations

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

def solution(n, wires):
    answer = float('inf')
    for w in combinations(wires, len(wires) - 1):
        parent = [i for i in range(n + 1)]
        for a, b in w:
            make_union(a, b, parent)
        
        root_counts = [0] * (n + 1)
        for i in range(1, n + 1):
            root = find_parent(i, parent)
            root_counts[root] += 1
        
        counts = [count for count in root_counts if count > 0]
        if len(counts) == 2:
            answer = min(answer, abs(counts[0] - counts[1]))
    
    return answer

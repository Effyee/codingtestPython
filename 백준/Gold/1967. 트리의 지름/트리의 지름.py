import sys

def dfs(start, tree, visited):
    stack = [(start, 0)]
    max_distance = [0, 0]

    while stack:
        node, distance = stack.pop()
        visited[node] = True

        if distance > max_distance[1]:
            max_distance = node, distance

        for next_node, weight in tree[node]:
            if not visited[next_node]:
                stack.append((next_node, distance + weight))

    return max_distance

n = int(sys.stdin.readline().rstrip())

tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, sys.stdin.readline().rsplit())
    tree[a].append((b, c))
    tree[b].append((a, c))

visited = [False] * (n+1)
farthest_node, _ = dfs(1, tree, visited)

visited = [False] * (n+1)
_, diameter = dfs(farthest_node, tree, visited)

print(diameter)

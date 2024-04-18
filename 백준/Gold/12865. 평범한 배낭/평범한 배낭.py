n, k = map(int, input().split())

data = []
for _ in range(n):
    w, v = map(int, input().split())
    data.append((w, v))

knapsack = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        w = data[i-1][0]
        v = data[i-1][1]

        if j < w:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(v + knapsack[i-1][j-w], knapsack[i-1][j])

print(knapsack[n][k])

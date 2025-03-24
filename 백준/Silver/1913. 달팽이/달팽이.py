N = int(input())
number = int(input())
snail = [[0] * N for _ in range(N)]

idx, c, n = 1, 1, 3
while idx <= N and n <= N:
    x, y = (N - idx) // 2, (N - idx) // 2

    up, down, left, right = n, n - 1, n - 1, n - 2
    snail[x][y] = c
    up -= 1
    c += 1
    x -= 1
    while right > 0:
        snail[x][y] = c
        c += 1
        right -= 1
        y += 1
    while down > 0:
        snail[x][y] = c
        c += 1
        down -= 1
        x += 1
    while left > 0:
        snail[x][y] = c
        c += 1
        left -= 1
        y -= 1
    while up > 0:
        snail[x][y] = c
        c += 1
        up -= 1
        x -= 1

    idx += 2
    n += 2

snail[0][0]=N*N
for row in snail:
    print(*row)

for x in range(N):
    for y in range(N):
        if snail[x][y]==number:
            print(x+1,y+1)
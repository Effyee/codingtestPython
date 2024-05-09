def check(x):
    for i in range(x):
        if row[x] == row[i] or abs(x - i) == abs(row[x] - row[i]):
            return False
    return True

def NQueen(x, N, row):
    global answer
    if x == N:
        answer += 1
        return
    else:
        for i in range(N):
            row[x] = i
            if check(x):
                NQueen(x + 1, N, row)

tc = int(input())

for _ in range(tc):
    N = int(input())
    row = [0] * N

    answer = 0

    NQueen(0, N, row)

    print(f'#{_+1} {answer}')

def check(x, row):
    for i in range(x):
        if row[i] == row[x] or abs(row[i] - row[x]) == abs(i - x):
            return False
    return True

def NQueen(x, n, row):
    global answer
    if x == n:
        answer += 1
        return
    else:
        for i in range(n):
            row[x] = i
            if check(x, row):
                NQueen(x + 1, n, row)

tc = int(input())

for _ in range(tc):
    n = int(input())
    row = [0] * n
    answer = 0
    NQueen(0, n, row)

    print(f'#{_ + 1} {answer}')

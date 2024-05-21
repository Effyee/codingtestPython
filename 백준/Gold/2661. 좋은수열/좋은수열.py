def check(sequence):
    length = len(sequence)
    for i in range(1, length // 2 + 1):
        if sequence[-i:] == sequence[-2 * i: -i]:
            return False
    return True

def dfs(sequence, n):
    if len(sequence) == n:
        print(sequence)
        return True

    for num in '123':
        if check(sequence + num):
            if dfs(sequence + num, n):
                return True

    return False

n = int(input().strip())
dfs('', n)
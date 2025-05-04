import sys
input = sys.stdin.readline

n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def check(line):
    used = [False] * n
    for i in range(n - 1):
        if line[i] == line[i + 1]:
            continue
        elif line[i] + 1 == line[i + 1]:  # 오르막
            for j in range(i, i - l, -1):
                if j < 0 or line[j] != line[i] or used[j]:
                    return False
                used[j] = True
        elif line[i] - 1 == line[i + 1]:  # 내리막
            for j in range(i + 1, i + 1 + l):
                if j >= n or line[j] != line[i + 1] or used[j]:
                    return False
                used[j] = True
        else:
            return False
    return True

answer = 0
for i in range(n):
    if check(graph[i]):       # 가로
        answer += 1
    if check([graph[j][i] for j in range(n)]):  # 세로
        answer += 1

print(answer)

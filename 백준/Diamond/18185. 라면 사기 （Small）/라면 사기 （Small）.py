import sys
input = sys.stdin.readline

n = int(input())
factories = list(map(int, input().split()))
answer = 0

for i in range(n - 2):
    if factories[i + 1] > factories[i + 2]:
        # 2연속 먼저 처리
        t = min(factories[i], factories[i + 1] - factories[i + 2])
        factories[i] -= t
        factories[i + 1] -= t
        answer += t * 5

    # 3연속 처리
    t = min(factories[i], factories[i + 1], factories[i + 2])
    factories[i] -= t
    factories[i + 1] -= t
    factories[i + 2] -= t
    answer += t * 7

# 남은 2연속 처리
for i in range(n - 1):
    t = min(factories[i], factories[i + 1])
    factories[i] -= t
    factories[i + 1] -= t
    answer += t * 5

# 남은 단독 처리
for i in range(n):
    answer += factories[i] * 3

print(answer)

import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

# 초기 상태 및 최종 상태 설정
final = list(input().strip())
start = sorted(final)

left_part = []
right_part = []

for _ in range(m):
    ladder = list(input().strip())

    if '?' in ladder:
        left_part = right_part[:]
        right_part = []
        continue
    right_part.append(ladder)

# '?' 이전 변환 (위에서 아래로)
for ladder in left_part:
    for i in range(n - 1):
        if ladder[i] == '-':
            start[i], start[i + 1] = start[i + 1], start[i]

# '?' 이후 변환 (아래에서 위로)
for ladder in reversed(right_part):
    for i in range(n - 1):
        if ladder[i] == '-':
            final[i], final[i + 1] = final[i + 1], final[i]

# '?'의 사다리 구성 찾기
answer = ['*'] * (n - 1)
for i in range(n - 1):
    if start[i] == final[i + 1] and start[i + 1] == final[i]:
        answer[i] = '-'
        start[i], start[i + 1] = start[i + 1], start[i]

# '?' 변환 후에도 start가 final과 다르면 불가능한 경우
if start != final:
    answer = ['x'] * (n - 1)

print(''.join(answer))

import sys
input = sys.stdin.readline

N = int(input())
schedules = []
for _ in range(N):
    start, end = map(int, input().split())
    schedules.append([start, end, end - start + 1])

# 정렬 (시작일 기준, 길이 내림차순)
schedules = sorted(schedules, key=lambda x: (x[0], -x[2]))

# 종료일은 모든 스케줄 중 가장 큰 값으로
start_date = min(schedule[0] for schedule in schedules)
end_date = max(schedule[1] for schedule in schedules)

height = [0] * (end_date + 1)

# 일정이 겹치는 날마다 높이 쌓기
for schedule in schedules:
    start, end = schedule[0], schedule[1]
    for i in range(start, end + 1):
        height[i] += 1

# 넓이 계산
answer = 0
i = start_date
while i < len(height):
    if height[i] == 0:
        i += 1
        continue
    w, h = 0, 0
    while i < len(height) and height[i] != 0:
        w += 1
        h = max(h, height[i])
        i += 1
    answer += w * h

print(answer)

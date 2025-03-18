import sys
input = sys.stdin.readline

# 입력 받기
N = int(input().strip())
events = [tuple(map(int, input().split())) for _ in range(N)]

# 1. 시작 날짜가 빠른 순으로 정렬, 같다면 종료 날짜가 긴 순으로 정렬
events.sort(key=lambda x: (x[0], -x[1]))

# 2. 날짜별로 몇 개의 일정이 있는지 기록할 배열
calendar = [0] * 366  # 1일부터 365일까지 사용

# 일정 배치
for s, e in events:
    for day in range(s, e + 1):
        calendar[day] += 1  # 해당 날짜의 일정 개수 증가

# 3. 코팅지 면적 계산
total_area = 0
width, max_height = 0, 0

for day in range(1, 366):
    if calendar[day] > 0:  # 일정이 있는 날이면
        width += 1
        max_height = max(max_height, calendar[day])
    else:  # 일정이 없는 날이면 이전 구간 종료
        if width > 0:
            total_area += width * max_height
        width, max_height = 0, 0  # 초기화

# 마지막 남은 일정 처리
if width > 0:
    total_area += width * max_height

# 정답 출력
print(total_area)

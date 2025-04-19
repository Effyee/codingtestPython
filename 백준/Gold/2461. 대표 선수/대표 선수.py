import sys
from collections import defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())
students = []

for i in range(n):
    scores = list(map(int, input().split()))
    for score in scores:
        students.append((score, i))  # (능력치, 반 번호)

# 능력치 기준 정렬
students.sort()

left = 0
min_diff = float('inf')
count_by_class = defaultdict(int)
num_classes_in_window = 0

for right in range(len(students)):
    score, cls = students[right]
    count_by_class[cls] += 1
    if count_by_class[cls] == 1:
        num_classes_in_window += 1

    # 모든 반이 포함되었으면 윈도우 줄이기 시도
    while num_classes_in_window == n:
        cur_diff = students[right][0] - students[left][0]
        min_diff = min(min_diff, cur_diff)

        # 왼쪽 포인터 이동
        count_by_class[students[left][1]] -= 1
        if count_by_class[students[left][1]] == 0:
            num_classes_in_window -= 1
        left += 1

print(min_diff)

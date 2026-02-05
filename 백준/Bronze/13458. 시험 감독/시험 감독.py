import sys
import math
input=sys.stdin.readline

n = int(input())
students = list(map(int, input().split()))
b, c = map(int, input().split())

answer = 0

for student in students:
    # 총감독관 1명
    student -= b
    # 부감독관 필요한 경우만 계산
    if student > 0:
        answer += math.ceil(student / c)

# 총감독관 n명 + 부감독관 answer명
print(answer + n)

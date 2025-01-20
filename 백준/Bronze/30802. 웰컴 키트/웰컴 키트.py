import sys
import math

# Input reading
input = sys.stdin.readline

# 참가자의 수
N = int(input().strip())

# 티셔츠 사이즈별 신청자의 수
sizes = list(map(int, input().strip().split()))

# 티셔츠 묶음 수와 펜 묶음 수
T, P = map(int, input().strip().split())

# 티셔츠를 최소 묶음 수로 주문하기 위해 계산
tshirt_bundles = 0
for size_count in sizes:
    tshirt_bundles += math.ceil(size_count / T)

# 펜을 최대 묶음 수로 주문하고 남은 펜 계산
pen_bundles = N // P
remaining_pens = N % P

# 출력
tshirts_output = tshirt_bundles
pens_output = f"{pen_bundles} {remaining_pens}"

# 결과 출력
print(tshirts_output)
print(pens_output)
import sys
from math import log2, ceil

# 표준 입력을 더 빠르게 읽기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

# N: 수의 개수, M: 수의 변경 횟수, K: 구간의 합 횟수
n, m, k = map(int, input().split())

# 원본 숫자들을 저장할 리스트
nums = [int(input()) for _ in range(n)]

# 세그먼트 트리의 높이 계산 (루트 노드의 높이를 0으로 간주)
# n개의 리프 노드를 가지는 완전 이진 트리의 높이 h는 ceil(log2(n))
h = ceil(log2(n))

# 세그먼트 트리를 저장할 배열
# 트리의 크기는 2^(h+1)로 설정하며, 이는 1-based 인덱싱을 사용할 때 충분한 크기임
tree = [0] * (2**(h + 1))

# 세그먼트 트리를 구축하는 함수
# start: 현재 노드가 담당하는 구간의 시작 인덱스 (nums 배열 기준)
# end: 현재 노드가 담당하는 구간의 끝 인덱스 (nums 배열 기준)
# node: 현재 세그먼트 트리 배열에서의 노드 인덱스 (1부터 시작)
def build(start, end, node):
    # 1. 리프 노드인 경우 (더 이상 쪼갤 수 없는 구간)
    if start == end:
        tree[node] = nums[start]
        return tree[node]
    else:
        # 2. 내부 노드인 경우 (쪼갤 수 있는 경우)
        mid = (start + end) // 2 # 구간을 절반으로 나눔
        # 왼쪽 자식과 오른쪽 자식의 합계를 현재 노드에 저장
        tree[node] = build(start, mid, node * 2) + build(mid + 1, end, node * 2 + 1)
        return tree[node]

# 구간 합을 구하는 함수
# start: 현재 노드가 담당하는 구간의 시작 인덱스
# end: 현재 노드가 담당하는 구간의 끝 인덱스
# left: 구하고 싶은 구간의 시작 인덱스 (0-기반)
# right: 구하고 싶은 구간의 끝 인덱스 (0-기반)
# node: 현재 세그먼트 트리 배열에서의 노드 인덱스
def query(start, end, left, right, node):
    # 현재 구간이 구하고 싶은 구간과 전혀 겹치지 않는 경우
    if left > end or right < start:
        return 0
    # 현재 구간이 구하고 싶은 구간에 완전히 포함되는 경우
    if left <= start and end <= right:
        return tree[node]
    else:
        # 현재 구간이 구하고 싶은 구간의 일부만 포함하거나, 더 큰 경우 (쪼개서 탐색)
        mid = (start + end) // 2
        return query(start, mid, left, right, node * 2) + query(mid + 1, end, left, right, node * 2 + 1)

# 값을 업데이트하는 함수
# target_idx: nums 배열에서 값을 변경할 실제 인덱스 (0-기반)
# value: target_idx에 설정할 새로운 값
# start, end: 현재 노드가 담당하는 구간
# node: 현재 세그먼트 트리 배열에서의 노드 인덱스
def update(target_idx, value, start, end, node):
    # 1. 리프 노드에 도달하여 변경 대상 인덱스를 찾은 경우
    if start == end:
        nums[target_idx] = value # 원본 배열도 업데이트
        tree[node] = value
        return

    # 2. 변경 대상 인덱스를 아직 찾지 못한 경우, 구간을 쪼개서 탐색
    mid = (start + end) // 2

    # 변경될 인덱스가 왼쪽 자식 구간에 속하는 경우
    if start <= target_idx <= mid:
        update(target_idx, value, start, mid, node * 2)
    # 변경될 인덱스가 오른쪽 자식 구간에 속하는 경우
    else: # mid + 1 <= target_idx <= end
        update(target_idx, value, mid + 1, end, node * 2 + 1)

    # 3. 자식 노드의 값이 변경되었으므로, 현재 노드의 값도 자식들의 합으로 갱신
    tree[node] = tree[node * 2] + tree[node * 2 + 1]

# 초기 세그먼트 트리 구축
build(0, n - 1, 1)

# M+K번의 연산 수행
for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        # a가 1인 경우: b번째 수를 c로 변경 (b는 1-기반 인덱스)
        # update 함수는 0-기반 인덱스를 받으므로 b-1로 변환
        update(b - 1, c, 0, n - 1, 1)
    else:
        # a가 2인 경우: b번째 수부터 c번째 수까지의 합 (b, c는 1-기반 인덱스)
        # query 함수는 0-기반 인덱스를 받으므로 b-1, c-1로 변환
        print(query(0, n - 1, b - 1, c - 1, 1))
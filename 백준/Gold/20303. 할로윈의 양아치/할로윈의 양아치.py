import sys
input = sys.stdin.readline

# 입력
n, m, k = map(int, input().split())
candy = [0] + list(map(int, input().split()))

parent = list(range(n+1))

# 유니온 파인드
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    pa, pb = find(a), find(b)
    if pa != pb:
        parent[pb] = pa

# 친구 관계 묶기
for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

# 그룹별 인원 수, 사탕 합 구하기
group_size = [0]*(n+1)
group_candy = [0]*(n+1)

for i in range(1, n+1):
    root = find(i)
    group_size[root] += 1
    group_candy[root] += candy[i]

#그룹 리스트
groups = []
for i in range(1, n+1):
    if group_size[i] > 0:
        groups.append((group_size[i], group_candy[i]))

dp = [0]*k  # k명 이상이면 안되니까 k-1까지만

for size, val in groups:
    for i in range(k-1, size-1, -1):
        dp[i] = max(dp[i], dp[i-size] + val)

print(max(dp))
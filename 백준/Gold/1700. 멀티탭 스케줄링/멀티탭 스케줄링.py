import sys
input=sys.stdin.readline

N, K = map(int, input().split())
order = list(map(int, input().split()))

plug = []  # 현재 콘센트에 꽂혀 있는 기기들
count = 0  # 뽑은 횟수

for i in range(K):
    curr = order[i]

    # 이미 꽂혀 있으면 패스
    if curr in plug:
        continue

    # 아직 자리 남아 있으면 꽂기
    if len(plug) < N:
        plug.append(curr)
        continue

    # 자리가 없으면, 앞으로 가장 늦게 쓰일 기기를 뺀다
    farthest = -1
    target = -1

    for p in plug:
        # 앞으로 또 사용되는지 확인
        if p in order[i+1:]:
            next_use = order[i+1:].index(p)
        else:
            next_use = K  # 다시 안 쓰이면 제일 먼 시점으로

        # 가장 나중에 쓰이는 기기 찾기
        if next_use > farthest:
            farthest = next_use
            target = p

    plug.remove(target)
    plug.append(curr)
    count += 1

print(count)

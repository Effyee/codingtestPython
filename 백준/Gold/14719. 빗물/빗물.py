H, W = map(int, input().split())
blocks = list(map(int, input().split()))

answer = 0
for i in range(1, W - 1):
    left_max = max(blocks[:i])
    right_max = max(blocks[i + 1:])
    water = min(left_max, right_max) - blocks[i]
    if water > 0:
        answer += water

print(answer)

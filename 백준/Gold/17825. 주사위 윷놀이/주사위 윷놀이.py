dice = list(map(int, input().split()))
answer = 0
# 점수 배열
score = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18,
         20, 22, 24, 26, 28, 30, 32, 34, 36, 38,
         40, 13, 16, 19, 25, 22, 24, 28, 27, 26,
         30, 35, 0]
# 4개의 경로
red = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 32]
blue10 = [5, 21, 22, 23, 24, 30, 31, 20, 32]
blue20 = [10, 25, 26, 24, 30, 31, 20, 32]
blue30 = [15, 27, 28, 29, 24, 30, 31, 20, 32]
# 갈림길 체크
switch = {5: blue10, 10: blue20, 15: blue30}
def backtrack(turn, horses, total):
    global answer
    if turn == 10:
        answer = max(answer, total)
        return

    for i in range(4):
        path, idx = horses[i]

        # 말이 이미 도착점이면 이동 불가
        if idx == len(path) - 1:
            continue

        # 이동
        next_idx = idx + dice[turn]
        next_path = path
        if next_idx >= len(path):
            next_idx = len(path) - 1  # 도착점

        # 갈림길 체크 (빨간길에서만)
        if path == red and path[idx] in switch:
            next_path = switch[path[idx]]
            next_idx = dice[turn]  # 파란길 진입 후 남은 이동
            if next_idx >= len(next_path):
                next_idx = len(next_path) - 1  # 도착점

        next_pos = next_path[next_idx]

        # 다른 말과 겹치면 이동 불가 (도착점 제외)
        if next_pos != 32 and any(h[1] < len(h[0]) - 1 and h[0][h[1]] == next_pos for j,h in enumerate(horses) if j != i):
            continue

        # 이동 실행
        before = horses[i]
        horses[i] = (next_path, next_idx)
        backtrack(turn + 1, horses, total + score[next_pos])
        horses[i] = before

backtrack(0, [(red, 0), (red, 0), (red, 0), (red, 0)], 0)
print(answer)

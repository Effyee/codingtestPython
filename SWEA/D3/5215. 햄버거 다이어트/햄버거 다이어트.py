def dfs(index, score, calorie):
    global max_score, N, L, ingredients
    # 제한 칼로리를 초과한 경우 더 이상 탐색하지 않음
    if calorie > L:
        return
    # 현재까지 조합의 점수가 최대 점수보다 큰 경우 업데이트
    if score > max_score:
        max_score = score
    # 모든 재료를 확인한 경우 탐색 종료
    if index == N:
        return
    # 현재 재료를 선택하는 경우
    dfs(index + 1, score + ingredients[index][0], calorie + ingredients[index][1])
    # 현재 재료를 선택하지 않는 경우
    dfs(index + 1, score, calorie)

# 입력
T = int(input())
for t in range(1, T+1):
    N, L = map(int, input().split())
    ingredients = [tuple(map(int, input().split())) for _ in range(N)]
    max_score = 0
    dfs(0, 0, 0)
    print(f"#{t} {max_score}")

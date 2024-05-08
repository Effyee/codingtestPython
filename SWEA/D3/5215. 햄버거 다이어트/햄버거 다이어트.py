T = int(input())

for case in range(1, T + 1):
    N, L = map(int, input().split())  # 재료의 수와 제한 칼로리를 입력받음
    ingredients = [list(map(int, input().split())) for _ in range(N)]  # 각 재료의 점수와 칼로리를 입력받음

    dp = [[0] * (L + 1) for _ in range(N + 1)]  # 동적 프로그래밍을 위한 테이블 초기화

    for i in range(1, N + 1):
        Ti, Ki = ingredients[i-1]
        for j in range(1, L + 1):
            if Ki <= j:  # 현재 재료를 추가할 수 있는 경우
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-Ki] + Ti)
            else:  # 현재 재료를 추가할 수 없는 경우
                dp[i][j] = dp[i-1][j]

    print(f'#{case} {dp[N][L]}')  # 결과 출력

tc = int(input())

for test_case in range(1, tc + 1):
    n, m = map(int, input().split())
    graph = []

    for _ in range(n):
        graph.append(list(map(int, input().split())))
    
    # 최대합을 저장할 변수 초기화
    max_sum = 0

    # 모든 가능한 m*m 부분 행렬에 대해 순회
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            # 현재 부분 행렬의 합을 계산
            current_sum = 0
            for k in range(m):
                for l in range(m):
                    current_sum += graph[i + k][j + l]
            
            # 최대합 업데이트
            max_sum = max(max_sum, current_sum)
    
    # 결과 출력
    print(f'#{test_case} {max_sum}')

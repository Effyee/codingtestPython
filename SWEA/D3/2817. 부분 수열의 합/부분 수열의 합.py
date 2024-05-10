def dfs(result, cnt):
    global answer
    if cnt == n:  # 모든 원소를 탐색했을 경우
        if result == k:  # 목표값에 도달했다면
            answer += 1
        return

    dfs(result + numbers[cnt], cnt + 1)  # 현재 원소를 포함하는 경우
    dfs(result, cnt + 1)  # 현재 원소를 포함하지 않는 경우

tc = int(input())

for _ in range(tc):
    n, k = map(int, input().split())  # 자연수의 개수, 목표값
    numbers = list(map(int, input().split()))

    answer = 0

    dfs(0, 0)

    print(f'#{_+1} {answer}')
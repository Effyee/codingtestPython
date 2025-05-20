t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    farm = [list(map(int, input().strip())) for _ in range(n)]
    half = n // 2
    answer = 0

    for i in range(0, half + 1):
        answer += sum(farm[i][half - i : half + i + 1])
    for i in range(half + 1, n):
        offset = i - half
        answer += sum(farm[i][offset : n - offset])

    print(f'#{tc} {answer}')
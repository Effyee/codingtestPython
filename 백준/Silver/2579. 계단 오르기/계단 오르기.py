def solution(n, score):
    answer = 0
    dp = [0] * 301

    dp[1] = score[1] #첫째 계단 초기 세팅(1번째 계단은 1번째 계단 밟는 게 최대)
    dp[2] = score[1] + score[2] #둘째 계단 초기 세팅(2번째 계단은 1번째 + 2번쨰 계단 밟는 게 최대)

    for i in range(3, n+1):  # 셋째 계단 이후부터 점화식 이용하여 최댓값 내기
				#1칸 전에서 온 경우(3칸 전 최댓값에서 + 2칸 이동한 1칸 전 값), 2칸 전에서 온 경우(2칸 전의 최댓값) 중 최댓값 + 현재 계단 값
        dp[i] = max(dp[i-3] + score[i -1], dp[i-2]) + score[i]

    answer = dp[n] #최대점수가 내장되어 있는 마지막 계단의 점수값이 답
    return answer 

if __name__ == "__main__":
    n = int(input())
    score = [0] * 301
    
    for i in range(1, n+1):
        score[i] = int(input())

    answer = solution(n,score)
    print(answer)
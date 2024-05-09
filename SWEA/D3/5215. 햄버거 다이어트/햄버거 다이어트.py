def dfs(total_taste,total_calorie,cnt):
    global answer
    if cnt==N:
        if total_calorie<L:
            answer=max(answer,total_taste)
        return
    dfs(total_taste+taste_score[cnt],total_calorie+calorie[cnt],cnt+1)
    dfs(total_taste,total_calorie,cnt+1)

tc=int(input())

for _ in range(tc):
    #재료의 수, 제한 칼로리
    N,L=map(int,input().split())
    taste_score=[]
    calorie=[]
    #맛 점수, 칼로리
    for i in range(N):
        score,cal=map(int,input().split())
        taste_score.append(score)
        calorie.append(cal)

    answer=0
    dfs(0,0,0)
    print(f'#{_+1} {answer}')
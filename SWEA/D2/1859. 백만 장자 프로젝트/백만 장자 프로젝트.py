t=int(input())

for _ in range(t):
    n=int(input())
    costs=list(map(int,input().split()))

    answer=0
    max_cost=costs[-1]
    for i in range(len(costs)-2,-1,-1):
        if costs[i]<max_cost:
            answer+=max_cost-costs[i]
        else:
            max_cost=costs[i]

    print(f'#{_+1} {answer}')

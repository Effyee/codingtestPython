tc=int(input())

for _ in range(tc):
    N=int(input())
    scores=list(map(int,input().split()))

    possible_scores={0}

    for score in scores:
        tmp=set()
        for ps in possible_scores:
            tmp.add(ps+score)
        possible_scores.update(tmp)

    print(f'#{_+1} {len(possible_scores)}')
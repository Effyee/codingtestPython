tc = int(input())

for _ in range(tc):
    n = int(input())
    scores = list(map(int, input().split()))

    possible_scores = {0}

    for score in scores:
        temp = set()
        for ps in possible_scores:
            temp.add(ps + score)
        possible_scores.update(temp)

    print(f'#{_ + 1} {len(possible_scores)}')

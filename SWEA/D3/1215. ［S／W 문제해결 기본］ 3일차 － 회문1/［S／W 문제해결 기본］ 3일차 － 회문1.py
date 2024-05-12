for _ in range(10):
    n=int(input())
    graph=[list(map(str,input().rstrip())) for _ in range(8)]

    letters=[]
    answer=0
    for i in range(8):
        letter=''
        for j in range(8-n+1):
            letters.append(''.join(map(str,graph[i][j:j+n])))

    for i in range(8):
        for j in range(8-n+1):
            letter=''
            for k in range(n):
                letter+=graph[k+j][i]
            letters.append(letter)

    for letter in letters:
        if letter==letter[::-1]:
            answer+=1

    print(f'#{_+1} {answer}')
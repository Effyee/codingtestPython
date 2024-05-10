tc=int(input())

for _ in range(tc):
    bit=list(map(int,input().strip()))

    #초기화 상태 000.. 에서 bit로 변경하는데 걸리는 횟수
    answer=0
    s=[0]*len(bit)
    for i in range(len(bit)):
        if bit[i]!=s[i]:
            answer+=1
            for j in range(i,len(bit)):
                s[j]=bit[i]
               
    print(f'#{_+1} {answer}')

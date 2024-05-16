for _ in range(10):
    tc=int(input())
    a,b=map(int,input().split())
    answer=a
    for i in range(b-1):
        answer*=a
    print(f'#{_+1} {answer}')
tc=10
for _ in range(tc):
    n=int(input())
    boxes=list(map(int,input().split()))

    while n>0:
        boxes.sort()
        boxes[0]+=1
        boxes[-1]-=1
        n-=1
    answer=max(boxes)-min(boxes)
    print(f'#{_+1} {answer}')

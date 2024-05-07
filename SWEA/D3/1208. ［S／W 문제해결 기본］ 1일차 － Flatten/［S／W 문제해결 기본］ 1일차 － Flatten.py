
for _ in range(10):
    n=int(input())
    boxes=list(map(int,input().split()))

    while n>0:
        boxes.sort()
        boxes[-1]-=1
        boxes[0]+=1
        n-=1

    boxes.sort()
    print(f'#{_+1} {boxes[-1]-boxes[0]}')
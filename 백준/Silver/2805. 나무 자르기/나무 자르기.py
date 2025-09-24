import sys
input=sys.stdin.readline

n,m=map(int,input().split())
tree=list(map(int,input().split()))

answer=0
start,end=1,max(tree)
while start<=end:
    mid=(start+end)//2
    result = sum(max(0, t - mid) for t in tree)
    # m 미터 이상의 나무가 확보된 경우, 답에 넣고
    # 높이를 늘린다
    if result>=m:
        answer=mid
        start=mid+1
    else:
        end=mid-1
print(answer)
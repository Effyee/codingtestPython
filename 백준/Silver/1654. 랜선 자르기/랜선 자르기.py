import sys
input=sys.stdin.readline
# 가지고 있는 랜선의 개수:k, 필요한 랜선의 개수:n
k,n=map(int,input().split())
li=[int(input()) for _ in range(k)]
li.sort()

def bs():
    start,end=1,max(li)
    answer=0
    while start<=end:
        cnt=0
        mid=(start+end)//2
        for i in range(k):
            cnt+=li[i]//mid
        if cnt>=n:
            answer=mid
            start=mid+1
        else:
            end=mid-1

    return answer

print(bs())
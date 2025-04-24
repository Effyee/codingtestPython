import sys
input=sys.stdin.readline

n,m,l=map(int,input().split())
arr=[0]
arr+=list(map(int,input().split()))
arr+=[l]

arr.sort()
answer=0
def bs():
    global answer
    start,end=1,l-1
    while start<=end:
        count=0
        mid=(start+end)//2
        for i in range(1,len(arr)):
            count+=(arr[i]-arr[i-1]-1)//mid
        if count > m:
            # 휴게소를 너무 많이 세워야 하니까 → 거리를 늘려야 함
            start = mid + 1
        else:
            # 조건 만족 → 답 후보로 저장하고 더 줄여보기
            answer = mid
            end = mid - 1
    return
bs()
print(answer)
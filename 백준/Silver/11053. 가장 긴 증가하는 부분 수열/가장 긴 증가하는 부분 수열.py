import sys
input=sys.stdin.readline

N=int(input())
arr=list(map(int,input().split()))
li=[arr[0]]

def binary_search(target,li):
    start,end=0,len(li)-1
    idx=0
    while start<=end:
        mid = (start + end) // 2
        # target보다 크거나 같은 값이 처음 나오는 곳
        if li[mid]<target:
            start=mid+1
        # 리스트의 숫자가 지금 숫자보다 크면
        else:
            end=mid-1
    return start

for i in range(1,N):
    target=arr[i]
    # 현재 숫자가 리스트의 마지막보다 크면 추가
    if arr[i]>li[-1]:
        li.append(arr[i])
    else:
        idx=binary_search(target,li)
        li[idx]=arr[i]

print(len(li))
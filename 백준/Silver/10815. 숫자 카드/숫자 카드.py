import sys
input=sys.stdin.readline

n=int(input())
cards= sorted(list(map(int, input().split())))

m=int(input())
nums=list(map(int,input().split()))

def binary_search(num):
    global answer
    start,end,flag=0,n-1,False
    while start<=end:
        mid=(start+end)//2
        if cards[mid]==num:
            answer.append(1)
            flag=True
            break
        elif cards[mid]<num:
            start=mid+1
        else:
            end=mid-1
    if not flag:
        answer.append(0)
answer=[]

for num in nums:
    binary_search(num)


print(' '.join(map(str, answer)))

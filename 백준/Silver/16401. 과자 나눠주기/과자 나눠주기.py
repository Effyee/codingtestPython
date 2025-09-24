import sys
input=sys.stdin.readline

# M명의 조카, N개의 과자, 조카 한명에게 줄 수 있는 막대 과자 최대길이
m,n=map(int,input().split())
snacks=list(map(int,input().split()))

#M개 이상의 과자를 만들되,M개가 만족되면 answer에 넣고나서 더 길게
start,end=1,max(snacks)
answer=0
while start<=end:
    mid=(start+end)//2
    count = sum(s // mid for s in snacks)
    if count>=m:
        answer=mid
        start=mid+1
    else:
        end=mid-1

print(answer)
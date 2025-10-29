import sys
input=sys.stdin.readline

n=int(input())
flowers=[list(map(int,input().split())) for _ in range(n)]
flowers.sort()

last_day=(3,1)
answer=0
i=0

while i<n:
    sm,sd,em,ed=flowers[i]
    if (sm,sd)<=last_day<=(em,ed):
        max_end_day=(em,ed)
        while i<n-1:
            nsm,nsd,nem,ned=flowers[i+1]
            if last_day<(nsm,nsd):
                break
            if max_end_day<(nem,ned):
                max_end_day=(nem,ned)
            i+=1
        answer+=1

        last_day=max_end_day
    if last_day>(11,30):
        print(answer)
        exit(0)
    i+=1

print(0)
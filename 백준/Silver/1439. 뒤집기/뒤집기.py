import sys

s=list(map(int,sys.stdin.readline().rstrip()))

answer=0
start=s[0]
for i in range(1,len(s)):
    if start==0:
        if s[i-1]==0 and s[i]==1:
            answer+=1
    else:
        if s[i - 1] == 1 and s[i] == 0:
            answer += 1

print(answer)
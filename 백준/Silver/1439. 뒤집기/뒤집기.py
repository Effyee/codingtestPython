import sys
input=sys.stdin.readline

# 연속된 하나의 숫자를 잡고 뒤집기
n=input().strip()
count=[0,0]
count[int(n[0])]+=1
standard=int(n[0])
for i in range(1,len(n)):
    if standard!=int(n[i]):
        if int(n[i])==1:
            count[1]+=1
            standard=1
        elif int(n[i])==0:
            count[0]+=1
            standard=0

if sum(count)==1:
    print(0)
else:
    print(min(count))
import sys
input=sys.stdin.readline

n=int(input())
A,B,C,D=[],[],[],[]
for _ in range(n):
    a,b,c,d=map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB=[]
CD=[]
for i in range(n):
    for j in range(n):
        AB.append(A[i]+B[j])
        CD.append(C[i]+D[j])

AB.sort()
CD.sort()

start,end=0,len(CD)-1
answer=0
while start<len(AB) and end>=0:
    re=AB[start]+CD[end]
    if re==0:
        count_a,count_b=0,0
        temp_start,temp_end=start,end
        while temp_start<len(AB) and AB[temp_start]==AB[start]:
            temp_start+=1
            count_a+=1
        while temp_end>=0 and CD[temp_end]==CD[end]:
            temp_end-=1
            count_b+=1
        answer+=count_a*count_b
        start=temp_start
        end=temp_end
    elif re<0:
        start+=1
    else:
        end-=1
print(answer)
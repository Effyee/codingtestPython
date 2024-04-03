import sys

n,m=map(int,input().split())

graph=[]

for _ in range(n):
    graph.append(list(map(str,sys.stdin.readline().strip())))

answer_row=0

for i in range(n):
    count=0
    for j in range(m):
        if graph[i][j]=='X':
            count+=1
        if j==m-1 and count==0:
            answer_row+=1

answer_col=0
for i in range(m):
    count=0
    for j in range(n):
        if graph[j][i]=='X':
            count+=1
        if j==n-1 and count==0:
            answer_col+=1

if answer_col>answer_row:
    print(answer_col)
else:
    print(answer_row)

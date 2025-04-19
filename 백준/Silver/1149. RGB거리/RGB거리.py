import sys
input=sys.stdin.readline

n=int(input())
values=[]
for _ in range(n):
    values.append(list(map(int,input().split())))

for i in range(1,n):
    values[i][0] = values[i][0] + min(values[i-1][1], values[i-1][2])
    values[i][1] = values[i][1] + min(values[i-1][0], values[i-1][2])
    values[i][2] = values[i][2] + min(values[i-1][0], values[i-1][1])

print(min(values[n-1]))
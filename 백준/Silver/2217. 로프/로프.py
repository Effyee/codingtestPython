import sys
input=sys.stdin.readline

n=int(input())
# k개의 로프를 사용해서 중량이 w인 물체를 들어올린다면,
# w/k 만큼 걸린다.

ropes=[int(input()) for _ in range(n)]
ropes=sorted(ropes,reverse=True)
answer=0
for i in range(n):
    answer=max(answer,(i+1)*ropes[i])
print(answer)
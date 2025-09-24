import sys
input=sys.stdin.readline

# 총 N개의 레벨, 각 레벨을 클리어할 때 마다 점수
# 쉬운 레벨이 어려운 레벨보다 점수를 많이 받는 경우가 있게 되었다.
# 특정 레벨의 점수를 감소시키려고 한다.

n=int(input())
arr=[int(input()) for _ in range(n)]
answer=0
for i in range(n-2,-1,-1):
    if arr[i]>=arr[i+1]:
        ori=arr[i]
        arr[i] = arr[i+1] - 1
        answer+=ori-arr[i]
    else:
        continue
print(answer)
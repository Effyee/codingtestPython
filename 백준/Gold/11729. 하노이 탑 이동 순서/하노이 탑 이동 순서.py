import sys
input=sys.stdin.readline

n=int(input())

def hanoi(start,end,middle,n,answer):
    if n==1:
        answer.append([start,end])
        return
    # 1. n-1개의 원판을 middle로 옮긴다. end가 보조기둥
    hanoi(start,middle,end,n-1,answer)
    # 2. n번째의 원판은 시작기둥에서 대상 기둥으로
    answer.append([start,end])
    # 3. n-1개가 옮겨졌던 middle이 시작기둥이 되고, n-1개를 n번째가 놓여진 end로 보내야한다.
    hanoi(middle,end,start,n-1,answer)
    return

answer=[]
hanoi(1,3,2,n,answer)
print(len(answer))
for a in answer:
    print(*a)
import sys
input=sys.stdin.readline

n=int(input())
eggs=[]
for _ in range(n):
    eggs.append(list(map(int,input().split())))

answer=0

def bt(idx):
    global answer
    if idx == n:
        broken = sum([1 for hp, _ in eggs if hp <= 0])
        answer = max(answer, broken)
        return

    if eggs[idx][0] <= 0:
        bt(idx + 1)
        return

    flag = False
    for i in range(n):
        if i == idx or eggs[i][0] <= 0:
            continue
        flag = True

        # 계란끼리 치기
        eggs[i][0] -= eggs[idx][1]
        eggs[idx][0] -= eggs[i][1]

        bt(idx + 1)

        # 상태 복구
        eggs[i][0] += eggs[idx][1]
        eggs[idx][0] += eggs[i][1]

    if not flag:
        bt(idx + 1)

bt(0)
print(answer)
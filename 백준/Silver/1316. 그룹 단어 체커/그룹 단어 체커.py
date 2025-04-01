import sys
input=sys.stdin.readline

n=int(input())
answer=0
for _ in range(n):
    word=str(input().rstrip())
    alphas={word[0]:1}
    for i in range(1,len(word)):
        if word[i] not in alphas:
            alphas[word[i]]=1
        elif word[i] in alphas:
            if word[i-1]!=word[i]:
                alphas[word[i]]=-1
    if len(alphas)==sum(alphas.values()):
        answer+=1

print(answer)
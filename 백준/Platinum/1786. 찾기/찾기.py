import sys
input=sys.stdin.readline

t = input().rstrip()
p = input().rstrip()

def make_pi():
    # 부분 문자열 에서 최대 prefix==suffix 길이를 담는 표
    pi=[0]*len(p)
    j=0
    for i in range(1,len(p)):
        # p[0..j-1]에서 다시 prefix==suffix의 길이를 찾기
        # 그 값이 왜 pi[j-1]일까?
        # pi[x]=p[0..x] 구간에서 prefix==suffix의 최대길이
        # p[0..j-1]에서 구하려면? pi[j-1]
        while j>0 and p[i]!=p[j]:
            j=pi[j-1]

        if p[i]==p[j]:
            j+=1
            pi[i]=j
    return pi

def solution(pi):
    result=[]
    count=0
    j=0
    for i in range(len(t)):
        while j>0 and t[i]!=p[j]:
            j=pi[j-1]

        if t[i]==p[j]:
            if j==(len(p)-1):
                count+=1
                result.append(i-len(p)+2)
                j=pi[j]
            else:
                j+=1
    return count,result

count,result=solution(make_pi())
print(count)
print(*result)
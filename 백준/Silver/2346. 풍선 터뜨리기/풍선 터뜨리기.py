import sys
def solution(n, l):
    i=0
    answer=[]
    l=[(num,idx+1) for idx,num in enumerate(l)]
    while l:
        j=l[i][0]
        answer.append(l.pop(i)[1])
        if len(l)==0:
            break
        if j<0:
            i=(i+j)%len(l)
        else:
            i=(i+j-1)%len(l)
    print(' '.join(map(str,answer)))

n = int(sys.stdin.readline())
l = list(map(int,sys.stdin.readline().split()))
solution(n, l)

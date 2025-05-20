n,m=map(int,input().split())
answer=set()
def bt(idx,li):
    if len(li)==m:
        answer.add(' '.join(map(str,li)))
        return
    if idx>n:
        return
    bt(idx+1,li+[idx])
    bt(idx+1,li)
    return

bt(1,[])
answer=sorted(list(answer))
for a in answer:
    print(a)
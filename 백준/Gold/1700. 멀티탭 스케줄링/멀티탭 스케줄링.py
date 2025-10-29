import sys
input=sys.stdin.readline

n,k=map(int,input().split())
arr=list(map(int,input().split()))
consent=[]
answer=0
for i in range(k):
    if arr[i] in consent:
        continue
    if len(consent)<n:
        consent.append(arr[i])
        continue

    target=-1
    farthest=-1

    for plugged in consent:
        if plugged not in arr[i+1:]:
            target=plugged
            break
        else:
            idx=arr[i+1:].index(plugged)
            if farthest<idx:
                farthest=idx
                target=plugged
    consent.remove(target)
    consent.append(arr[i])
    answer+=1

print(answer)

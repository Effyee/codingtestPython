n=list(map(int,input().rstrip()))

mid=len(n)//2

if sum(n[:mid])==sum(n[mid:]):
    print('LUCKY')
else:
    print('READY')
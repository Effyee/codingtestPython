def solution(info, n, m):
    answer = 0
    INF=int(1e9)
    arr=[INF]*m
    arr[0]=0
    for A,B in info:
        new_arr=[INF]*m
        for b in range(m):
            if arr[b]==INF:
                continue
            # A가 훔침
            if arr[b]+A<n:
                new_arr[b]=min(new_arr[b],arr[b]+A)
            # B가 훔침
            if b+B<m:
                new_arr[b+B]=min(arr[b],new_arr[b+B])
        arr=new_arr
        
    res=min(arr)
    return res if res<INF else -1
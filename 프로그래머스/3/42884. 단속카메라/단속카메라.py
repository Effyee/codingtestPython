def solution(routes):
    answer = 0
    routes=sorted(routes,key=lambda x:x[0])
    start,end=routes[0]
    new=[]
    for i in range(1,len(routes)):
        if start<=routes[i][0]<=end:
            start=max(start,routes[i][0])
            end=min(end,routes[i][1])
            print(start,end)
        else:
            new.append([start,end])
            start,end=routes[i]

    return len(new)+1
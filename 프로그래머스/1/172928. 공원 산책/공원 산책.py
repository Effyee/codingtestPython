def solution(park, routes):
    answer = []
    dir={
        'N':(-1,0),
        'S':(1,0),
        'W':(0,-1),
        'E':(0,1)
    }
    park=[list(park[i]) for i in range(0,len(park))]
    
    #시작지점 초기화
    x,y=0,0
    
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j]=='S':
                x,y=i,j
                break;
    
    
    for route in routes:
        d,c=route.split()
        c=int(c)
        nx,ny=x,y
        dx,dy=dir[d]
        for i in range(c):
            if(0<=nx+dx<len(park) and 0<=ny+dy<len(park[0]) and park[nx+dx][ny+dy]!='X'):
                nx=nx+dx
                ny=ny+dy
            else:
                nx,ny=x,y
                break
        x,y=nx,ny
            
    return [x,y]
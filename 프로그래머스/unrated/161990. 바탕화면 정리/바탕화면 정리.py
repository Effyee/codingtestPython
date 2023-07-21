def solution(wallpaper):
    r,c=[],[]
    w,h=len(wallpaper),len(wallpaper[0])
    for i in range(w):
        for j in range(h):
            if str(wallpaper[i][j])=="#":
                r.append(i)
                c.append(j)
                
    return (min(r),min(c),max(r)+1,max(c)+1)
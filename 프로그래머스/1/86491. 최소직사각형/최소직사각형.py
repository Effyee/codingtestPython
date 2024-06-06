def solution(sizes):
    sorted_size=[]
    for size in sizes:
        size.sort(reverse=True)
        sorted_size.append(size)
    max_r,max_w=0,0
    for s in sorted_size:
        w,r=s
        if w>max_w:
            max_w=w
        if r>max_r:
            max_r=r
    return max_r*max_w
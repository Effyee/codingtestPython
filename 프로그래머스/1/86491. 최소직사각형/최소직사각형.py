def solution(sizes):
    answer = 0
    sorted_size=[]
    for size in sizes:
        a,b=size
        if a<=b:
            sorted_size.append([b,a])
        else:
            sorted_size.append([a,b])
    sorted_size.sort(reverse=True)
    print(sorted_size[0][0])
    m=0
    for s in sorted_size:
        if m<s[1]:
            m=s[1]
    return sorted_size[0][0]*m
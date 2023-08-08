def solution(sizes):
    answer = 0
    sorted_sizes=[]
    #가장 긴 길이를 하고
    #가로 세로중에 긴 길이인 부분을 [x,y] x부분에 놓고 긴 길이 안에 들어오게
    #[x,y] 부분 중에 
    for size in sizes:
        sorted_sizes.append(sorted(size))
        
    w_max=0
    h_max=0
    for i in range(len(sorted_sizes)):
        if sorted_sizes[i][1]>w_max:
            w_max=sorted_sizes[i][1]
        if sorted_sizes[i][0]>h_max:
            h_max=sorted_sizes[i][0]
    return (h_max*w_max)
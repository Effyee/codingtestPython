def solution(name):
    answer = 0
    for char in name:
        answer+=min(ord(char)-ord('A'),ord('Z')-ord(char)+1)

    n=len(name)
    cursor=n-1

    for i in range(n):
        next_idx=i+1
        while next_idx<n and name[next_idx]=='A':
            next_idx+=1
        cursor=min(cursor,2*i+n-next_idx,i+2*n-2*next_idx)
    answer+=cursor
    return answer
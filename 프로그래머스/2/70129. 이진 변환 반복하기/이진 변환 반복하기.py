def solution(s):
    lst=list(map(int,list(s)))
    r,b=0,0
    while len(lst)!=1:
        n_lst=[num for num in lst if num==1]
        r+=len(lst)-len(n_lst)
        binary=list(bin(len(n_lst)))
        binary=binary[2:]
        b+=1
        lst=list(map(int,binary))

    return [b,r]
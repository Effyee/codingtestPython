nums=[]
for _ in range(9):
    nums.append(int(input()))
answer=[]
def backtrack(idx,l):
    global answer
    if len(l)==7:
        if sum(l)==100:
            l.sort()
            for i in range(7):
                print(l[i])
            exit()
        return

    if idx>8:
        return

    l.append(nums[idx])
    backtrack(idx+1,l)
    l.pop()
    backtrack(idx+1,l)
    return

backtrack(0,[])

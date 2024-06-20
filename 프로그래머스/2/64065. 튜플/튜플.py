def solution(s):
    number=[]
    nums=[]
    answer = [0] * len(nums)
    m=''
    for i in range(len(s)):
        if s[i]=='{' or s[i]=='}' or s[i]==',':
            if m:
                number.append(int(m))
                if int(m) not in nums:
                    nums.append(int(m))
                m=''
        else:
            m+=s[i]
    cnt=[0]*(max(number)+1)

    for n in number:
        cnt[n]+=1

    
    for i in range(len(nums),0,-1):
        answer.append(cnt.index(i))

    return answer
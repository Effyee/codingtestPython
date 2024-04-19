def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2 + 1):  
        l = make_list(s, i)
        result = make_shorteds(l)
        if len(result) < answer:
            answer = len(result)
    
    return answer

def make_list(s, length):
    l = []
    for i in range(0, len(s), length):
        l.append(s[i:i+length])
    return l

def make_shorteds(l):
    cnt = 1
    result = ''
    for i in range(1, len(l)):
        if l[i-1] == l[i]:
            cnt += 1
        else:
            if cnt >= 2:
                result += str(cnt) + l[i-1]
            else:
                result += l[i-1]
            cnt = 1
    result += str(cnt) + l[len(l)-1] if cnt >= 2 else l[len(l)-1]
    return result

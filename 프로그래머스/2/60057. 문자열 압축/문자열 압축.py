INF = int(1e9)

def solution(s):
    answer = INF
    if len(s) == 1:  
        return 1
    for i in range(1, len(s)//2 + 1):
        l = cutted_list(s, i)
        answer = min(answer, make_shortened(l))
    return answer

def cutted_list(s, length):
    l = []
    for i in range(0, len(s), length):
        l.append(s[i:i+length])
    return l

def make_shortened(l):
    cnt = 1
    result = ''
    for i in range(1, len(l)):
        if l[i-1] == l[i]:
            cnt += 1
        else:
            if cnt >= 2:
                result += str(cnt) + l[i-1]
                cnt = 1
            else:
                result += l[i-1]
    if cnt >= 2:
        result += str(cnt) + l[-1]
    else:
        result += l[-1]
    return len(result)

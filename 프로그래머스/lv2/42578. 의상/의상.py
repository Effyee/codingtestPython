def solution(clothes):
    answer = 0
    dic={}
    for cloth in clothes:
        if cloth[1] in dic:
            dic[cloth[1]]+=1
        else:
            dic[cloth[1]]=1
    
    for i in dic:
        if answer == 0:
            answer = dic[i] + 1
            print(answer)
        else:
            answer *= (dic[i] + 1)

    answer -= 1
    return answer
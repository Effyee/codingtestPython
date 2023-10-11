def solution(s):
    answer = 0
    i = 0

    while i < len(s):
        x = s[i]
        count_x = 0
        count_not_x = 0

        while i < len(s) and (count_x == 0 or count_x != count_not_x):
            if s[i] == x:
                count_x += 1
            else:
                count_not_x += 1
            
            i += 1
        
        answer += 1

    return answer

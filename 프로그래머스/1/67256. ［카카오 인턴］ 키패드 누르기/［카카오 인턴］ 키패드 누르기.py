def solution(numbers, hand):
    answer = ''
    key_dict = {1:(0,0), 2:(0,1), 3:(0,2),
                4:(1,0), 5:(1,1), 6:(1,2),
                7:(2,0), 8:(2,1), 9:(2,2),
                '*':(3,0), 0:(3,1), '#':(3,2)}
    
    left = [1, 4, 7]
    right = [3, 6, 9]
    lhand = '*'
    rhand = '#'
    
    for num in numbers:
        if num in left:
            answer += 'L'
            lhand = num
        elif num in right:
            answer += 'R'
            rhand = num
        else:
            curPos = key_dict[num]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])
            
            if ldist < rdist:
                answer += 'L'
                lhand = num
            elif ldist > rdist:
                answer += 'R'
                rhand = num
            else:
                if hand == "left":
                    answer += 'L'
                    lhand = num
                else:
                    answer += 'R'
                    rhand = num
    return answer

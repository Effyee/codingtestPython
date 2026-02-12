def solution(numbers, hand):
    answer = ''
    
    # 키패드 좌표 매핑
    keypad = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        '*':(3,0), 0:(3,1), '#':(3,2)
    }
    
    # 시작 위치
    left = keypad['*']
    right = keypad['#']
    
    for num in numbers:
        # 왼쪽 열
        if num in [1,4,7]:
            answer += 'L'
            left = keypad[num]
        
        # 오른쪽 열
        elif num in [3,6,9]:
            answer += 'R'
            right = keypad[num]
        
        # 가운데 열
        else:
            target = keypad[num]
            
            # 맨해튼 거리 계산
            left_dist = abs(left[0] - target[0]) + abs(left[1] - target[1])
            right_dist = abs(right[0] - target[0]) + abs(right[1] - target[1])
            
            if left_dist < right_dist:
                answer += 'L'
                left = target
            elif right_dist < left_dist:
                answer += 'R'
                right = target
            else:
                if hand == "right":
                    answer += 'R'
                    right = target
                else:
                    answer += 'L'
                    left = target
    
    return answer

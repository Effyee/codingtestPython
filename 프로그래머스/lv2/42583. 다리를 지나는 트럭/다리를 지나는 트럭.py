def solution(bridge_length, weight, truck_weights):
    time = 0
    p = list(truck_weights) # 트럭 무게
    x = [0] * bridge_length # 다리
    s=0
    while (x):
        time += 1
        s-=x.pop(0) # s: 다리 위의 총 트럭 무게
        if p:
            if ( s + p[0] ) <= weight:
                s+=p[0] # 여유되면 트럭 추가
                x.append(p.pop(0)) # 다리에 트럭 추가  
            else:
                x.append(0) # 여유 없으면 무게 0 추가

    return time
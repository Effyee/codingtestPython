def solution(bridge_length, weight, truck_weights):
    answer = 1
    bridge=[[truck_weights.pop(0),0]]
    while bridge or truck_weights:
        answer+=1
        w=0
        if bridge:
            for i in range(len(bridge)):
                w+=bridge[i][0]
                bridge[i][1]+=1
            if bridge[0][1]==bridge_length-1:
                bridge.pop(0)
        if truck_weights:
            if w+truck_weights[0]<=weight and len(bridge)<=bridge_length:
                bridge.append([truck_weights.pop(0),0])

    return answer+1
def solution(bridge_length, weight, truck_weights):
    day, total_weight = 0, 0
    bridge = []  # 다리를 건너는 트럭을 표현할 리스트
    while bridge or truck_weights:  # 다리 위에 트럭이 있거나 대기 중인 트럭이 있는 경우
        day += 1

        # 다리에서 나가는 트럭 처리
        if bridge and bridge[0][1] + 1 > bridge_length:  # 첫 번째 트럭이 다리를 건넜는지 확인
            truck_weight,_  = bridge.pop(0)  # 다리를 건넌 트럭 제거
            total_weight -= truck_weight  # 다리 위의 총 무게 감소

        # 새로운 트럭이 다리에 올라갈 수 있는지 확인
        if truck_weights and total_weight + truck_weights[0] <= weight and len(bridge)+1<=bridge_length:  # 다리의 무게 한도 확인
            truck_weight = truck_weights.pop(0)  # 대기 중인 트럭 중 첫 번째 트럭 선택
            bridge.append([truck_weight, 0])  # 다리에 트럭 추가
            total_weight += truck_weight  # 다리 위의 총 무게 증가

        # 다리를 건너는 모든 트럭의 위치 업데이트
        for i in range(len(bridge)):
            bridge[i][1] += 1  # 각 트럭의 위치를 1 증가
    return day  # 모든 트럭이 다리를 건넌 후의 총 일수 반환
from collections import defaultdict
from math import ceil

# 입차, 출차 기록이 주어졌을 때, 차량별로 주차 요금 계산
def solution(fees, records):
    answer = []
    records.sort()  # 시간순 정렬
    
    cars = defaultdict(list)
    st, sf, ct, cf = fees  # 기본시간, 기본요금, 단위시간, 단위요금
    
    # 차량별 시간 저장
    for record in records:
        time, car_num, status = record.split()
        cars[int(car_num)].append(time)
    
    # 출차 기록 없는 차량은 23:59 추가
    for k in cars:
        if len(cars[k]) % 2 == 1:
            cars[k].append('23:59')
    
    # 🚨 차량번호 오름차순 정렬
    for k in sorted(cars.keys()):
        v = cars[k]
        total_time = 0
        
        # 누적 주차 시간 계산
        for i in range(0, len(v), 2):
            sh, sm = map(int, v[i].split(':'))
            eh, em = map(int, v[i+1].split(':'))
            
            start = sh * 60 + sm
            end = eh * 60 + em
            
            total_time += (end - start)
        
        # 요금 계산
        if total_time <= st:
            answer.append(sf)
        else:
            extra = ceil((total_time - st) / ct)
            answer.append(sf + extra * cf)
    
    return answer

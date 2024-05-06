def find_max(building):
    max_index=0
    second_index=0
    for i in range(5):
        if building[max_index]<building[i]:
            max_index=i

    return max_index

for _ in range(10):
    n=int(input())
    buildings=list(map(int,input().split()))

    answer=0
    for i in range(n-4):
        building=buildings[i:i+5]
        max_index=find_max(building)
        sorted_building=sorted(building)
        if max_index==2:
            answer+=building[max_index]-sorted_building[-2]

    print('#'+str(_+1)+' '+str(answer))

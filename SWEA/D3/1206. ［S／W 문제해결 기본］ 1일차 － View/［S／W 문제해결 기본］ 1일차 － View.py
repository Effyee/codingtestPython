def find_max(lst):
    max_index=0
    for i in range(1,5):
        if lst[max_index]<lst[i]:
            max_index=i
    return max_index

for _ in range(10):
    n=int(input())
    buildings=list(map(int,input().split()))
    answer=0
    for i in range(n-4):
        building=buildings[i:i+5]
        sorted_building=sorted(building)

        if find_max(building)==2:
            answer+=building[2]-sorted_building[-2]

    print(f'#{_+1} {answer}')

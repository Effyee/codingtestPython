parent = []
def find(x):
    global parent
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    global parent
    a = find(a)
    b = find(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
def solution(n, wires):
    global parent
    answer = 10000001  
    
    for i in range(len(wires)):
        parent = [i for i in range(n+1)]
        for j in range(len(wires)):
            if i != j and find(wires[j][0]) != find(wires[j][1]):
                union(wires[j][0], wires[j][1])
        
        group_dict = {}
        
        for i in range(1,n+1):
            if find(i) not in group_dict:
                group_dict[find(i)] = 1
            else:
                group_dict[find(i)] += 1
                
        a,b = group_dict.values()
        
        answer = min(answer, abs(a - b))
        
    return answer
from collections import defaultdict
def solution(players, callings):
    rank={}
    
    for i,player in enumerate(players):
        rank[player]=i
    
    for calling in callings:
        idx=rank[calling]
        front_player=players[idx-1]
        players[idx-1],players[idx]=players[idx],players[idx-1]
        
        rank[calling]-=1
        rank[front_player]+=1
        
    return players
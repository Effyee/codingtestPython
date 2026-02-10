def solution(users, emoticons):
    answer = []
    discount_ratio=[10,20,30,40]
    e,t=0,0
    
    def count(dis_ratio):
        total,eplus=0,0        
        for user in users:
            t,p=0,0
            # 기준 할인률, 기준 총액
            percent, cost=user
            #print(f'할인률:{dis_ratio}')
            #print(f'기준 할인률:{percent}, 기준 총액:{cost} ')
            for i in range(len(dis_ratio)):
                # user의 기준 할인률 보다 할인을 많이 하면
                if dis_ratio[i]>=percent:
                    t+=emoticons[i]*((100-dis_ratio[i])/100)
            # 지금까지 산 이모티콘 총액이 기준액 이상이면 패스를 구매
            if t>=cost:
                eplus+=1
            # 이하이면 총액에 더하기
            else:
                total+=t
        #print(f'플러스 개수:{eplus},총액:{total}')
        
        return [eplus,total]
    
    def bf(li):
        nonlocal e
        nonlocal t
        if len(li)==len(emoticons):
            eplus,total=count(li)
            if e<eplus:
                e=eplus
                t=total
            elif e==eplus:
                if t<total:
                    t=total
            return
        for i in range(4):
            li.append(discount_ratio[i])
            bf(li)
            li.pop()
        return
    
    bf([])
    return [e,t]
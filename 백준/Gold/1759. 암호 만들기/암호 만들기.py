def dfs(result,index):
    global words
    if len(result)==l or index==c:
        if len(result)==l and result not in words:
            words.append(result)
        return
    dfs(result+alphabets[index],index+1)
    dfs(result,index+1)



l,c=map(int,input().split())
alphabets=list(map(str,input().split()))
words=[]
alphabets.sort()
dfs('',0)
answers=[]
for word in words:
    t1,t2=0,0
    for w in word:
        if w in ['a','e','o','u','i']:
            t1+=1
        else:
            t2+=1
    if t1>0 and t2>1:
        answers.append(word)

for answer in answers:
    print(answer)


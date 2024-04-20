n=int(input())

datas=[]

for _ in range(n):
    name,korean,english,math=input().split()
    datas.append((name,korean,english,math))

datas=sorted(datas,key= lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for data in datas:
    print(data[0])



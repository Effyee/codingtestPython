n = int(input())

members = []
for i in range(n):
    age, name = input().split()
    members.append((int(age), i, name))

members.sort() 

for age, _, name in members:
    print(f'{age} {name}')

import sys
input = sys.stdin.readline

sounds = list(input().strip())
ducks = []

for s in sounds:
    found = False
    for duck in ducks:
        if s == 'q' and duck[-1] == 'k':
            duck.clear()
        if s == 'q' and not duck:
            duck.append('q')
            found = True
            break
        elif duck and s == 'u' and duck[-1] == 'q':
            duck.append('u')
            found = True
            break
        elif duck and s == 'a' and duck[-1] == 'u':
            duck.append('a')
            found = True
            break
        elif duck and s == 'c' and duck[-1] == 'a':
            duck.append('c')
            found = True
            break
        elif duck and s == 'k' and duck[-1] == 'c':
            duck.append('k')
            found = True
            break
    if not found:
        if s == 'q':
            ducks.append(['q'])
        else:
            print(-1)
            exit(0)


for duck in ducks:
    if duck and duck[-1] != 'k':
        print(-1)
        exit(0)

print(len(ducks))

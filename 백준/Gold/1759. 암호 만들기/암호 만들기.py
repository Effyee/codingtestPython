def dfs(result, index):
    global passwords

    if len(result) == l or index == len(word):
        if result not in passwords and len(result) == l:
            passwords.append(result)
        return

    dfs(result + word[index], index + 1)
    dfs(result, index + 1)


# 암호 길이, 문자의 종류
l, c = map(int, input().split())

word = list(map(str, input().split()))
word.sort()

passwords = []
dfs("", 0)
password = []

for word in passwords:
    t1, t2 = 0, 0
    for w in word:
        if w in ['a', 'e', 'i', 'o', 'u']:
            t1 += 1
        elif w in ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']:
            t2 += 1
    if t1 >= 1 and t2 >= 2:
        password.append(word)

for p in password:
    print(p)

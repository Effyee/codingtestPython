import sys

input = sys.stdin.readline

L, C = map(int, input().split())
letters = list(input().split())
letters.sort()
answer = []


def backtrack(pw, idx):
    if len(pw) == L:
        vowel = 0
        consonant = 0
        for c in pw:
            if c in {'a', 'e', 'i', 'o', 'u'}:
                vowel += 1
            else:
                consonant += 1
        if vowel >= 1 and consonant >= 2:
            answer.append(pw)
        return

    if idx >= C:
        return

    # 현재 글자 포함하는 경우
    backtrack(pw + letters[idx], idx + 1)
    # 현재 글자 포함하지 않는 경우
    backtrack(pw, idx + 1)


backtrack('', 0)

for pwd in answer:
    print(pwd)

def restore_permutation(s):
    def backtrack(index, path):
        if index == len(s):
            return path

        for length in range(1, 3):
            if index + length <= len(s):
                num = int(s[index:index + length])
                if 1 <= num <= n and num not in used:
                    used.add(num)
                    result = backtrack(index + length, path + [num])
                    if result:
                        return result
                    used.remove(num)
        return None

    n = min(50, len(s))
    used = set()
    result = backtrack(0, [])
    return result


s = input().strip()
result = restore_permutation(s)
print(' '.join(map(str, result)))

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] not in stack:
                # 스택의 마지막 문자보다 현재 문자가 작고, 스택의 마지막 문자가 이후에도 등장한다면 제거
                while stack and ord(s[i]) < ord(stack[-1]) and stack[-1] in s[i+1:]:
                    stack.pop()
                stack.append(s[i])
        return "".join(stack)

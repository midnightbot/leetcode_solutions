class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for x in range(len(s)):
            stack.append(s[x])
            if stack and len(stack) >=2 and (stack[-2]+stack[-1] == 'AB' or stack[-2] + stack[-1] == 'CD'):
                stack.pop()
                stack.pop()

        return len(stack)

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for x in s:
            if x in '1234567890':
                stack.pop()
            else:
                stack.append(x)

        return "".join(stack)
        

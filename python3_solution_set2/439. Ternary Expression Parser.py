class Solution:
    def parseTernary(self, exp: str) -> str:

        lens = len(exp) - 1
        stack = []

        while lens >=0:
            c = exp[lens]
            if c in '1234567890TF':
                stack.append(c)
                lens-=1
            elif c == ':':
                lens-=1
            elif c == '?':
                lens-=1
                left_part = stack.pop()
                right_part = stack.pop()
                if exp[lens] == 'T':
                    stack.append(left_part)
                else:
                    stack.append(right_part)
                lens-=1
        return stack[-1]
        

class Solution:
    def minChanges(self, s: str) -> int:
        # greedy solution
        ans = 0
        stack = []
        for x in s:
            if not stack:
                stack.append(x)
            elif stack[-1] == x:
                stack.append(x)
            else:
                if len(stack)%2!=0:
                    ans+=1
                    stack = []
                else:
                    stack = [x]

        return ans
        

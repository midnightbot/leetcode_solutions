class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        stack = []

        for x in nums:
            if len(stack) < 3:
                stack.append(x)
            else:
                if stack[-3] != 1:
                    count+=1
                    stack[-3] = 1
                    stack[-2] = (stack[-2]+1)%2 
                    stack[-1] = (stack[-1]+1)%2 
                stack.append(x)

        if stack[-3] != 1:
            count+=1
            stack[-3] = 1
            stack[-2] = (stack[-2]+1)%2 
            stack[-1] = (stack[-1]+1)%2
        return count if (stack[-1]==1 and stack[-2]==1) else -1
        

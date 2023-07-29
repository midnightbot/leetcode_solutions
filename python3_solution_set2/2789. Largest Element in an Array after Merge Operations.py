class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        nums = nums[::-1]
        stack = []

        for x in nums:
            stack.append(x)
            if len(stack) >=2:
                if stack[-2] >= stack[-1]:
                    top = stack.pop()
                    stack[-1]+=top

        return max(stack)

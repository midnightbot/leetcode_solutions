class Solution:
    def canSortArray(self, nums: List[int]) -> bool:

        nums = [[x,format(x,'b').count('1')] for x in nums]
        stack = []
        # print(nums)
        for (x,y) in nums:
            # print(stack)
            if not stack:
                stack.append((x,y))
            else:
                # either correct position
                if x >= stack[-1][0]:
                    stack.append((x,y))

                # or need to switch
                else:
                    removed = []
                    while stack and stack[-1][0] > x:
                        if stack[-1][1] == y:
                            (a,b) = stack.pop()
                            removed.append((a,b))
                        else:
                            return False
                    stack.append((x,y))
                    for (a,b) in removed[::-1]:
                        stack.append((a,b))
        return True
        

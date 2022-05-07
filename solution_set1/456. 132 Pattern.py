class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        if len(nums) < 3:
            return False
        
        stack = []
        pre = [-1 for x in range(len(nums))] ## prefix array for mins
        
        pre[0] = nums[0]
        
        for x in range(1,len(nums)):
            pre[x] = min(pre[x-1], nums[x])
            
        for x in range(len(nums)-1,-1,-1):
            
            if nums[x] <= pre[x]:
                continue
                
            while stack and stack[-1] <= pre[x]:
                stack.pop()
                
            if stack and stack[-1] < nums[x]:
                return True
            
            stack.append(nums[x])
            
        return False
            
        

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        #count  = 0
        ans = []
        for x in range(len(nums)):
            if nums[x]!= 0:
                ans.append(nums[x])
                
        n = len(nums)
        m = len(ans)
        
        for x in range(n-m):
            ans.append(0)
            
        for x in range(len(ans)):
            nums[x] = ans[x]
                
        
        

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        maxs = nums[0]
        mins = nums[0]
        ans = maxs
        
        for x in range(1,len(nums)):
            temp = max(nums[x],maxs*nums[x],mins*nums[x])
            mins = min(nums[x],maxs*nums[x],mins*nums[x])
            
            maxs = temp
            
            ans = max(ans,maxs)
        
        
        return ans

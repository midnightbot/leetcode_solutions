class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        
        idx1 = nums.index(min(nums))
        idx2 = nums.index(max(nums))
        
        if idx1 > idx2:
            ## ans = min(removing from left and right, removing from left, removing from right)
            ans = min(idx2+1+(len(nums)-idx1),idx1+1,len(nums)-idx2)
            
        else:
            ans = min(idx1+1+(len(nums)-idx2),idx2+1,len(nums)-idx1)
            
        return ans
            
        
        

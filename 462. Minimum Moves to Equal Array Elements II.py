class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        
        ans = 0
        
        nums = sorted(nums)
        median = nums[len(nums)//2]
        for x in range(len(nums)):
            ans+=abs(nums[x] - median)
            
        return ans
                
        
        
        

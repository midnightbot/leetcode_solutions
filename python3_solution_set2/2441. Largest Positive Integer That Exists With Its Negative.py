class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        nums = set(nums)
        ans = -1
        for x in range(1,1001):
            if x in nums and -x in nums:
                ans = x
                
        return ans
        

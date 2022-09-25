class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        ans = max(nums)
        c = 0
        result = 0
        for x in nums:
            if x == ans:
                c+=1
                
            else:
                c = 0
                
            
            result = max(result, c)
            
        return result

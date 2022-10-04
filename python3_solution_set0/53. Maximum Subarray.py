class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        current_ans = nums[0]
        max_ans = nums[0]
        for x in range(1,len(nums)):
            current_ans = max(current_ans+nums[x], nums[x])
            max_ans = max(max_ans, current_ans)
            
        return max_ans
            
        

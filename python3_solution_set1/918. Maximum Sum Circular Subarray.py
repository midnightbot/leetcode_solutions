class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        def max_subarray(nums):
            current_ans = nums[0]
            max_ans = nums[0]
            for x in range(1,len(nums)):
                current_ans = max(current_ans+nums[x], nums[x])
                max_ans = max(max_ans, current_ans)
                
            #print(max_ans)
            return max_ans
        
        
        if len(nums) == 1:
            return nums[0]
        
        sums = sum(nums)
        
        temp = max_subarray(nums)
        temp2 = sums + max_subarray([-x for x in nums][1:])
        temp3 = sums + max_subarray([-x for x in nums][0:-1])
        
        return max(temp,temp2,temp3)

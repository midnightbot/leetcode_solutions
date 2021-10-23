class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = [-1] * len(nums)
        
        left_ans = [-1] * len(nums)
        right_ans = [-1] * len(nums)
        
        left_ans[0] = 1
        right_ans[len(nums)-1] = 1
        
        for x in range(1,len(nums)):
            left_ans[x] = left_ans[x-1] * nums[x-1]
            
        for x in range(len(nums)-2,-1,-1):
            right_ans[x] = right_ans[x+1] * nums[x+1]
            
        for x in range(len(nums)):
            ans[x] = left_ans[x] * right_ans[x]
            
        return ans

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ## all nums in array will be equal to nums[-1]
        ans = 0

        for x in range(len(nums)-1):
            if nums[x]!=nums[x+1]:
                ans+=1
        return ans
        

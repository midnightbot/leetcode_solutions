class Solution:
    def countSubarrays(self, nums: List[int]) -> int:

        ans = 0
        for x in range(len(nums)-2):
            temp1 = nums[x] + nums[x+2]
            temp2 = nums[x+1]
            if temp1 == temp2/2:
                ans+=1
        return ans
        

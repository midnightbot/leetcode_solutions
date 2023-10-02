class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0

        for x in range(len(nums)-2):
            for y in range(x+1, len(nums)-1):
                for z in range(y+1, len(nums)):
                    ans = max(ans, (nums[x] - nums[y]) * nums[z])
        return ans
        

##ss
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        
        nums = sorted(nums, reverse = True)
        
        total = sum(nums)
        
        ans = []
        inc = 0
        for x in range(len(nums)):
            inc+=nums[x]
            total -= nums[x]
            ans.append(nums[x])
            if inc > total:
                return ans
        

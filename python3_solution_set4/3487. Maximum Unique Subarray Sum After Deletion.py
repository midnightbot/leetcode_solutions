class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if max(nums) <= 0:
            return max(nums)

        else:
            seen = set()

            for x in nums:
                if x>0:
                    seen.add(x)
            return sum(seen)
        

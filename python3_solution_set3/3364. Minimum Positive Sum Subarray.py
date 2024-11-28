class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:

        ans = float('inf')

        for x in range(len(nums)):
            for y in range(x+1, len(nums)+1):
                temp = sum(nums[x:y])
                if l <= y-x <= r:
                    if temp > 0:
                        ans = min(ans, temp)
                

        return ans if ans!=float('inf') else -1

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = float('inf')

        for x in range(len(nums)):
            for y in range(x,len(nums)):
                res = reduce(lambda x, y: x | y, nums[x:y+1])
                if res >= k:
                    ans = min(ans, y-x+1)

        return ans if ans!=float('inf') else -1
        

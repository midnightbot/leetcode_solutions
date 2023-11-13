class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        ans = 0

        for x in range(len(nums)):
            for y in range(len(nums)):
                if abs(nums[x]-nums[y]) <= min(nums[x], nums[y]):
                    ans = max(ans, nums[x] ^ nums[y])
        return ans
        

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:

        nums.sort()
        seen = set()

        for x in range(len(nums)//2):
            seen.add(nums[x] + nums[-x-1])
        return len(seen)

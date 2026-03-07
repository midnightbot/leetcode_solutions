class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ans = []
        mins, maxs = min(nums), max(nums)
        nums = set(nums)

        for x in range(mins, maxs+1):
            if x not in nums:
                ans.append(x)
        return ans
        
